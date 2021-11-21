"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: noviembre 2021
Programa: mainIntermedio.py
Propósito: Programa de nueva version del main anterior
V 2.0
"""

# ZONA DE IMPORTS
from decafAlejandrov2Lexer import decafAlejandroV2Lexer
from decafAlejandroV2Parser import decafAlejandroV2Parser
from decafAlejandroV2Listener import decafAlejandroV2Listener
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from funciones import *
from ErrorClass import *
from nodoBoolean import NodoBooleano
from symbolTable import *
import emoji
import sys
from pprint import pprint
from itertools import groupby
from symbolTable import *
# we import Node
from NodoCodigo import *
from nodoBoolean import *
import pickle


class MyErrorListener(ErrorListener):
    def __init__(self):
        self.hasErrors = False
        self.lexicalErrors = []
        super(MyErrorListener, self).__init__()
        pass

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hasErrors = True
        errorMsg = str(line) + ":" + str(column) + \
            ": sintaxis ERROR encontrado " + str(msg)
        self.lexicalErrors.append(errorMsg)

    def getHasError(self):
        return self.hasErrors


class DecafAlejandroPrinter(decafAlejandroV2Listener):
    def __init__(self):
        self.root = None
        # data types primitivos
        self.BOOLEAN = 'boolean'
        self.VOID = 'void'
        self.STRING = 'char'
        self.INT = 'int'
        self.ERROR = 'error'
        # un diccionario con primitivos
        self.data_type = {
            'char': self.STRING,
            'int': self.INT,
            'boolean': self.BOOLEAN,
            'void': self.VOID,
            'error': self.ERROR
        }
        # variables distintas
        self.ambitos = []
        self.scope_Actual = None
        self.metodos = []
        self.metodosV2 = []
        self.metodo_Actual = "GLOBAL"
        self.tablaVariables = dictTableVars()
        self.errores = SemanticError()
        self.tabla_metodos = dictTableMetods()
        self.tabla_estructuras = dictTableStruct()
        self.tabla_parametros = tableDictParameters()

        # ? generacion codigo intermedio variables
        self.tipoNodo = {}  # el tipo de nodo de cada valor que iteraremos
        self.dictCodigoIntermedio = {}  # el tipo de nodo de cada valor que iteraremos
        self.contadorGlobalNodos = 0
        self.contadorTemporales = 0
        self.arrayProduccionesTerminadas = []
        self.contadorGTrue = 0
        self.contadorWhile = 0
        super().__init__()

    def popScope(self):
        self.scope_Actual.valueToTable()
        self.scope_Actual = self.ambitos.pop()

    def addScope(self):
        self.ambitos.append(self.scope_Actual)
        self.scope_Actual = generalSymbolTableV2()

    def popMethodActual(self):
        self.metodo_Actual = self.metodos.pop()

    def addMethodActual(self, metodo):
        self.metodo_Actual = metodo
        self.metodos.append(metodo)
        self.metodosV2.append(metodo)

    def findVar(self, variable):
        """
        *@param variable: busca la variable en el scope actual
        """
        innerArray = []
        innerVar = self.scope_Actual.getSymbolFromTable(variable)
        if innerVar == 0:
            innerArray = self.ambitos.copy()
            innerArray.reverse()
            for scope in innerArray:
                innerVar2 = scope.getSymbolFromTable(variable)
                if innerVar2 != 0:
                    return innerVar2
            return 0
        else:
            return innerVar

    def findVarV2(self, variable):
        """
        *@param variable: busca la variable en el scope actual, retorna en DONDE lo halló
        """
        innerArray = []
        founded = ""
        innerVar = self.scope_Actual.getSymbolFromTable(variable)
        if innerVar == 0:
            innerArray = self.ambitos.copy()
            innerArray.reverse()
            for scope in innerArray:
                innerVar2 = scope.getSymbolFromTable(variable)
                if innerVar2 != 0:
                    if(innerVar2["Scope"] == "GLOBAL"):
                        return innerVar2, "GLOBAL"
                    else:
                        return innerVar2, "ANOTHER"
            return 0
        else:
            if(innerVar["Scope"] == "GLOBAL"):
                founded = "GLOBAL"
            else:
                founded = "ANOTHER"
            return innerVar, founded

    def generateTopeGet(self, varId):
        """
        Toma un varID y genera el código fp[offset] o gp[offset] de la misma
        *@param varId: el id de la variable
        """
        variable, contexto = self.findVarV2(varId)
        innerString = ""
        if(contexto == "GLOBAL"):
            innerString = f'G[{variable["Offset"]}]'
        elif(contexto == "ANOTHER"):
            innerString = f'fp[{variable["Offset"]}]'
        return innerString

    def generateTemporal(self):
        """
        Retorna una nueva temporal
        """
        temporal = ""
        temporal = f't{self.contadorTemporales}'
        self.contadorTemporales += 1
        return temporal

    def Intersection(self, a, b):
        """
        Realiza la interseccion de dos valores
        """
        return [v for v in a if v in b]

    def all_equal(self, iterable):
        """
        Iterable es la variable que busca el valor
        """
        g = groupby(iterable)
        return next(g, True) and not next(g, False)

    def ChildrenHasError(self, ctx):
        """
        REvisa que el hijo tenga errores. Retorna TRUE si hay o FALSE si no
        *@param ctx: el contexto
        """
        non_terminals = [self.tipoNodo[i] for i in ctx.children if type(
            i) in [decafAlejandroV2Parser.LocationContext,
                   decafAlejandroV2Parser.ExprContext,
                   decafAlejandroV2Parser.BlockContext,
                   decafAlejandroV2Parser.DeclarationContext]]
        if self.ERROR in non_terminals:
            return True
        return False

    def enterProgram(self, ctx: decafAlejandroV2Parser.ProgramContext):
        print('----------> INICIO COMPILACION <--------------')
        self.root = ctx
        self.scope_Actual = generalSymbolTableV2()

    def enterMethod_declr(self, ctx: decafAlejandroV2Parser.Method_declrContext):
        metodo = ctx.method_name().getText()
        parameters = []

        if self.tabla_metodos.getSymbolFromTable(metodo) == 0:
            # ALEJANDRO CHANGES ---
            self.addMethodActual(metodo)
            self.arrayProduccionesTerminadas.append(f'DEF {metodo.upper()}:\n')
            # <--------->
            if ctx.return_type().var_type() is not None:
                tipo = ctx.return_type().var_type().getText()
            else:
                tipo = ctx.return_type().getText()
            hijos = ctx.getChildCount()

            for i in range(hijos):
                if isinstance(ctx.getChild(i), decafAlejandroV2Parser.Var_typeContext):
                    typeParameter = self.data_type[ctx.getChild(i).getText()]
                    idParameter = ctx.getChild(i + 1).getText()

                    parameters.append(
                        {'Tipo': typeParameter, 'Id': idParameter})
                    self.tabla_parametros.AddEntryToTable(
                        typeParameter, idParameter)

            self.tabla_metodos.AddEntryToTable(tipo, metodo, parameters, None, 0)

        self.addScope()

        for parameter in parameters:
            type_symbol = self.tablaVariables.getSymbolFromTable(
                parameter['Tipo'])
            size = type_symbol['Size']
            offset = self.scope_Actual.offsetVariables
            self.scope_Actual.AddEntryToTable(
                parameter['Tipo'], parameter['Id'], size, offset, True, self.metodo_Actual)

    def exitMethod_declr(self, ctx: decafAlejandroV2Parser.Method_declrContext):
        metodo = ctx.method_name().getText()
        name = ctx.method_name().getText()
        size_scope = self.scope_Actual.getSize() # obtenemos el size del método
        self.tabla_metodos.addSizeToMethodTable(size_scope, self.metodo_Actual)
        self.arrayProduccionesTerminadas.append(f'END DEF {name.upper()} \n\n')
        # <--------->
        self.tabla_parametros.cleanTable()
        self.popScope()
        # ALEJANDRO CHANGES ---
        self.popMethodActual()
        self.tipoNodo[ctx] = self.VOID
        self.dictCodigoIntermedio[ctx] = ctx

    def enterVardeclr(self, ctx: decafAlejandroV2Parser.VardeclrContext):
        tipo = ctx.var_type().getText()

        # TOMAR EN CUENTA DECLARACION DE ARRAY'S
        if ctx.field_var().var_id() is not None:
            id = ctx.field_var().var_id().getText()

            # Si no encuentra una variable, la guarda en la tabla de simbolos
            # En caso contrario, ya está declarada, y eso es ERROR.

            if self.tabla_parametros.getSymbolFromTable(id) != 0:
                self.tipoNodo[ctx] = self.ERROR
                self.tipoNodo[ctx.field_var()] = self.ERROR
                line = ctx.field_var().var_id().start.line
                col = ctx.field_var().var_id().start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_VAR_REPETIDA)
                return

            if self.scope_Actual.getSymbolFromTable(id) == 0:
                type_symbol = self.tablaVariables.getSymbolFromTable(tipo)
                if type_symbol == 0:
                    line = ctx.var_type().start.line
                    col = ctx.var_type().start.column
                    self.errores.AddEntryToTable(
                        line, col, f'El tipo {tipo} de variable no ha sido declarado previamente..')
                    self.tipoNodo[ctx] = self.ERROR
                    self.tipoNodo[ctx.field_var()] = self.ERROR
                    return
                size = type_symbol['Size']
                offset = self.scope_Actual.offsetVariables

                self.scope_Actual.AddEntryToTable(
                    tipo, id, size, offset, False, self.metodo_Actual)
            else:
                self.tipoNodo[ctx] = self.ERROR
                self.tipoNodo[ctx.field_var()] = self.ERROR
                line = ctx.field_var().var_id().start.line
                col = ctx.field_var().var_id().start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_VARDUPLICADA)
        elif ctx.field_var().array_id() is not None:
            id = ctx.field_var().array_id().getChild(0).getText()

            if self.tabla_parametros.getSymbolFromTable(id) != 0:
                self.tipoNodo[ctx] = self.ERROR
                self.tipoNodo[ctx.field_var()] = self.ERROR
                line = ctx.field_var().var_id().start.line
                col = ctx.field_var().var_id().start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_VAR_REPETIDA)
                return

            if self.scope_Actual.getSymbolFromTable(id) == 0:
                type_symbol = self.tablaVariables.getSymbolFromTable(tipo)
                if type_symbol == 0:
                    line = ctx.var_type().start.line
                    col = ctx.var_type().start.column
                    self.errores.AddEntryToTable(
                        line, col, f'El tipo {tipo} de variable no ha sido declarado previamente.')
                    self.tipoNodo[ctx] = self.ERROR
                    self.tipoNodo[ctx.field_var()] = self.ERROR
                    return

                tipo_array = 'array' + tipo
                size = 0

                if ctx.field_var().array_id().int_literal() is not None:
                    size = int(
                        ctx.field_var().array_id().int_literal().getText())
                    # agregamos el size del valor
                    innerSize = 0
                    innerSize = self.tablaVariables.getSymbolFromTable(tipo)[
                        "Size"]
                    if(innerSize != 0):
                        size = size * innerSize

                if 'struct' in tipo_array:
                    self.tablaVariables.AddEntryToTable(
                        tipo_array, size, self.tablaVariables.ARRAY + self.tablaVariables.STRUCT)
                else:
                    self.tablaVariables.AddEntryToTable(
                        tipo_array, size, self.tablaVariables.ARRAY)

                type_symbol = self.tablaVariables.getSymbolFromTable(
                    tipo_array)

                size = type_symbol['Size']
                offset = self.scope_Actual.offsetVariables

                self.scope_Actual.AddEntryToTable(
                    tipo_array, id, size, offset, False, self.metodo_Actual)

            else:
                self.tipoNodo[ctx] = self.ERROR
                self.tipoNodo[ctx.field_var()] = self.ERROR
                line = ctx.field_var().var_id().start.line
                col = ctx.field_var().var_id().start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_VARDUPLICADA)

    def enterStruct_declr(self, cstx: decafAlejandroV2Parser.Struct_declrContext):
        self.addScope()

    def exitStruct_declr(self, ctx: decafAlejandroV2Parser.Struct_declrContext):
        tipo = ctx.getChild(0).getText() + ctx.getChild(1).getText()

        if self.tablaVariables.getSymbolFromTable(tipo) == 0:
            size_scope = self.scope_Actual.getSize()
            self.tablaVariables.AddEntryToTable(
                tipo, size_scope, self.tablaVariables.STRUCT)
            self.tabla_estructuras.ExtractInfo(
                tipo, self.scope_Actual, self.tablaVariables)
            self.popScope()

            self.tipoNodo[ctx] = self.VOID
            for child in ctx.children:
                if not isinstance(child, TerminalNode):
                    if self.tipoNodo[child] == self.ERROR:
                        self.tipoNodo[ctx] = self.ERROR
                        break
        else:
            self.tipoNodo[ctx] = self.ERROR
            line = ctx.start.line
            col = ctx.start.column
            self.errores.AddEntryToTable(
                line, col, self.errores.errrorText_VARDUPLICADA)

    def enterVar_id(self, ctx: decafAlejandroV2Parser.Var_idContext):
        parent = ctx.parentCtx
        if parent in self.tipoNodo.keys():
            self.tipoNodo[ctx] = self.tipoNodo[parent]
            # we double the instruction -ALEJANDRO CHANGES
            #self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[parent]

    def exitVar_id(self, ctx: decafAlejandroV2Parser.Var_idContext):
        """ parent = ctx.parentCtx
        if parent in self.tipoNodo.keys() or ctx in self.tipoNodo.keys():
            return """
        id = ctx.getText()
        variable = self.findVar(id)
        # creamos el nodo
        nodoInner = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        nodoInner.addCode("")  # por regla semantica E.codigo = ""
        """ print("codigo generado de : ",
              variable["Id"], "  ", self.generateTopeGet(variable["Id"])) """
        # por regla semantica E.dir = tope.get (id.lexema)
        nodoInner.addAddress(self.generateTopeGet(variable["Id"]))
        # agregamos al dict global
        self.dictCodigoIntermedio[ctx] = nodoInner

        # ! quizas podamos borrar esto
        """ if variable['Tipo'] in [self.INT, self.STRING, self.BOOLEAN]:
            self.tipoNodo[ctx] = self.data_type[variable['Tipo']]
        else:
            self.tipoNodo[ctx] = self.VOID """

    def exitVardeclr(self, ctx: decafAlejandroV2Parser.VardeclrContext):
        self.tipoNodo[ctx] = self.VOID
        self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            1)]

    def exitString_literal(self, ctx: decafAlejandroV2Parser.String_literalContext):
        self.tipoNodo[ctx] = self.STRING
        # creamos un nuevo nodo
        nodoS = Nodo(self.contadorGlobalNodos)
        nodoS.addAddress(ctx.getText())
        self.contadorGlobalNodos += 1
        self.dictCodigoIntermedio[ctx] = nodoS

    def exitInt_literal(self, ctx: decafAlejandroV2Parser.Int_literalContext):
        self.tipoNodo[ctx] = self.INT
        # creamos un nuevo nodo
        nodoS = Nodo(self.contadorGlobalNodos)
        nodoS.addAddress(ctx.getText())
        self.contadorGlobalNodos += 1
        self.dictCodigoIntermedio[ctx] = nodoS

    def exitBool_literal(self, ctx: decafAlejandroV2Parser.Bool_literalContext):
        self.tipoNodo[ctx] = self.BOOLEAN
        # creamos un nuevo nodo
        nodoS = Nodo(self.contadorGlobalNodos)
        nodoS.addAddress(ctx.getText())
        self.contadorGlobalNodos += 1
        self.dictCodigoIntermedio[ctx] = nodoS

    def exitLiteral(self, ctx: decafAlejandroV2Parser.LiteralContext):
        self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]
        self.tipoNodo[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]

    def enterArray_id(self, ctx: decafAlejandroV2Parser.Array_idContext):
        parent = ctx.parentCtx
        if parent in self.tipoNodo.keys():
            self.tipoNodo[ctx] = self.tipoNodo[parent]

    def exitArray_id(self, ctx: decafAlejandroV2Parser.Array_idContext):
        parent = ctx.parentCtx
        """ if parent in self.tipoNodo.keys() or ctx in self.tipoNodo.keys():
            return """
        id = ctx.getChild(0).getText()
        variable = self.findVar(id)
        tipo = variable['Tipo']
        if ctx.int_literal() is not None:
            if 'array' in tipo:
                if tipo.split('array')[-1] in [self.INT, self.STRING, self.BOOLEAN]:
                    self.tipoNodo[ctx] = self.data_type[tipo.split(
                        'array')[-1]]
                else:
                    self.tipoNodo[ctx] = self.VOID
        elif ctx.var_id() is not None:
            tipo = variable['Tipo']
            tipo_var = self.findVar(ctx.var_id().getText())
            self.CheckErrorInArrayId(ctx, tipo, tipo_var)
        """
        New logic
        """
        if not isinstance(parent, decafAlejandroV2Parser.Field_varContext):
            name = ctx.ID().getText()
            variable = self.findVar(name)
            tipo = variable['Tipo']
            tipo = tipo.split('array')[-1]
            nodo = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
            Expression = 0
            if ctx.int_literal():
                Expression = self.dictCodigoIntermedio[ctx.int_literal()]
            elif ctx.var_id():
                Expression = self.dictCodigoIntermedio[ctx.var_id()]
            cantTipo = 0

            if tipo == 'int':
                cantTipo = 4
            elif tipo == 'char':
                cantTipo = 2
            elif tipo == 'boolean':
                cantTipo = 1
            temp1 = self.generateTemporal()
            temp2 = self.generateTemporal()
            offset = variable["Offset"]
            nodo.addAddress(self.generateLabelforArray(variable, temp2))
            codigoConcat = ' ' + Expression.getCode() + \
                (str(temp1) + ' = ' + str(cantTipo) + ' * ' + Expression.getAddress()) + '\n ' + \
                (str(temp2) + ' = ' + str(offset) + ' + ' + str(temp1)) + '\n'
            nodo.addCode(codigoConcat)
        else:
            nodo = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
        self.dictCodigoIntermedio[ctx] = nodo

    def exitVar_type(self, ctx: decafAlejandroV2Parser.Var_typeContext):
        self.tipoNodo[ctx] = self.VOID

    def exitField_var(self, ctx: decafAlejandroV2Parser.Field_varContext):
        """ if ctx not in self.tipoNodo.keys():
            if ctx.var_id() is not None:
                self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)]
            elif ctx.array_id() is not None:
                self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)] """

        if ctx not in self.dictCodigoIntermedio.keys():
            if ctx.var_id() is not None:
                self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
                    0)]
            elif ctx.array_id() is not None:
                self.dictCodigoIntermedio[ctx] = self.tipoNodo[ctx.getChild(0)]

    def enterField_declr(self, ctx: decafAlejandroV2Parser.Field_declrContext):
        tipo = ctx.var_type().getText()

        for child in ctx.children:
            if not isinstance(child, TerminalNode) and isinstance(child, decafAlejandroV2Parser.Field_varContext):
                id = child.var_id().getText()

                if self.scope_Actual.getSymbolFromTable(id) == 0:
                    type_symbol = self.tablaVariables.getSymbolFromTable(tipo)
                    size = type_symbol['Size']
                    offset = self.scope_Actual.offsetVariables

                    self.scope_Actual.AddEntryToTable(
                        tipo, id, size, offset, False, self.metodo_Actual)

    def exitField_declr(self, ctx: decafAlejandroV2Parser.Field_declrContext):
        self.tipoNodo[ctx] = self.VOID
        for child in ctx.children:
            if not isinstance(child, TerminalNode):
                if self.tipoNodo[child] == self.ERROR:
                    self.tipoNodo[ctx] = self.ERROR
                    break

    def enterBlock(self, ctx: decafAlejandroV2Parser.BlockContext):
        parent = ctx.parentCtx

        if not isinstance(parent, decafAlejandroV2Parser.Method_declrContext):
            self.addScope()
            self.addMethodActual("BLOCK")

    def exitBlock(self, ctx: decafAlejandroV2Parser.BlockContext):
        parent = ctx.parentCtx
        if not isinstance(parent, decafAlejandroV2Parser.Method_declrContext):
            self.popScope()
            # ALEJANDRO CHANGES ---
            self.popMethodActual()

        longitud = len(ctx.statement())
        acumuladoNuevo = ""
        nodoNuevo = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        for x in range(0, longitud):
            # acumulamos codigo
            acumuladoNuevo = acumuladoNuevo + "\n " +\
                self.dictCodigoIntermedio[ctx.statement()[x]].getCode()
        nodoNuevo.addCode(acumuladoNuevo)
        #print("ACUMULADO NUEVO ", acumuladoNuevo)
        self.dictCodigoIntermedio[ctx] = nodoNuevo

    def visitNodes(self, params):
        innerArray = []
        for param in params:
            innerNode = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
            innerNode.addCode('')
            paramName = param.getText()
            if isinstance(param, decafAlejandroV2Parser.Expr_methodCallContext):
                paramName = param.method_call().method_name().getText()
            elif isinstance(param, decafAlejandroV2Parser.Expr_locationContext):
                if param.location().array_id() is not None:
                    paramName = param.location().array_id().ID().getText()
            if isinstance(param, decafAlejandroV2Parser.Expr_PrecedenciaMenorContext) or isinstance(param, decafAlejandroV2Parser.Expr_PrecedenciaMaxContext):
                print("OPERACION")
                hijo = self.dictCodigoIntermedio[param]
                innerNode.addCode(hijo.getCode())
                innerNode.addAddress(hijo.getAddress())
            else:
                print("LOCATION VAR NORMAL")
                if self.findVar(paramName) != 0:
                    variable = self.findVar(paramName)
                    if("array" in variable["Tipo"]):  # si es array
                        if param.location().array_id().int_literal():
                            Expression = self.dictCodigoIntermedio[param.location(
                            ).array_id().int_literal()]
                        elif param.location().array_id().var_id():
                            Expression = self.dictCodigoIntermedio[param.location(
                            ).array_id().var_id()]
                        arrayType = variable['Tipo']
                        arrayType = arrayType.split('array')[-1]
                        pesoVar = 0
                        if arrayType == 'int':
                            pesoVar = 4
                        elif arrayType == 'char':
                            pesoVar = 2
                        elif arrayType == 'boolean':
                            pesoVar = 1
                        temp1 = self.generateTemporal()
                        temp2 = self.generateTemporal()
                        offset = variable["Offset"]
                        innerNode.addAddress(
                            self.generateLabelforArray(variable, temp2))
                        codigoConcat = ' ' + Expression.getCode() + \
                            (str(temp1) + ' = ' + str(pesoVar) + ' * ' + Expression.getAddress()) + '\n ' + \
                            (str(temp2) + ' = ' + str(offset) +
                             ' + ' + str(temp1)) + '\n'
                        innerNode.addCode(codigoConcat)
                    else:
                        innerNode.addAddress(
                            self.generateTopeGet(variable["Id"]))
                elif paramName in self.metodosV2:
                    method_info = self.tabla_metodos.getSymbolFromTable(
                        paramName)
                    codigoConcat = ' CALL ' + paramName + ', ' + \
                        str(len(method_info["Parameters"])) + '\n'
                    innerNode.addCode(codigoConcat)
                    innerNode.addAddress("R")
                else:
                    innerNode.addAddress(paramName)
            innerArray.append(innerNode)

        return innerArray

    def exitMethod_call(self, ctx: decafAlejandroV2Parser.Method_callContext):
        name = ctx.method_name().getText()
        parameters = []
        nombre = name
        # si es una suma y creamos un nodoo nuevo
        nodoLlamada = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        args = self.visitNodes(ctx.expr())
        for arg in args:
            codigo = nodoLlamada.getCode()
            codigo += arg.getCode() + (' PARAM ' + arg.getAddress() + '\n')
            nodoLlamada.addCode(codigo)

        codigo = nodoLlamada.getCode()
        codigo += ' CALL ' + nombre + ', ' + str(len(args)) + '\n'
        nodoLlamada.addCode(codigo)
        nodoLlamada.addAddress("R")
        self.dictCodigoIntermedio[ctx] = nodoLlamada

        """ for child in ctx.children:
            if isinstance(child, decafAlejandroV2Parser.ExprContext):
                parameters.append(child)

        method_info = self.tabla_metodos.getSymbolFromTable(name)
        if len(parameters) == 0:
            self.tipoNodo[ctx] = method_info['Tipo']
            return

        self.tipoNodo[ctx] = method_info['Tipo'] """

    def GetMethodType(self, ctx):
        nodo = ctx.parentCtx
        hijos = [str(type(i))
                 for i in nodo.children if not isinstance(i, TerminalNode)]
        while str(decafAlejandroV2Parser.Return_typeContext) not in hijos:
            nodo = nodo.parentCtx
            hijos = [str(type(i))
                     for i in nodo.children if not isinstance(i, TerminalNode)]

        if nodo.return_type().var_type() is not None:
            return nodo.return_type().var_type().getText()
        else:
            return nodo.return_type().getText()

    def generateLabelforWhile(self, valor):
        innerValue = ''
        if valor == 'startwhile':
            innerValue = f'WHILE_LOOP_{self.contadorWhile}'
        elif valor == 'endwhile':
            print('entra')
            innerValue = f'END_WHILE_{self.contadorWhile}'
            self.contadorWhile += 1
        elif valor == 'true':
            innerValue = f'IF_TRUE_{self.contadorGTrue}'
        elif valor == 'false':
            innerValue = f'IF_FALSE_{self.contadorGTrue}'
            self.contadorGTrue += 1
        else:
            innerValue = f'{valor}:'

        return innerValue

    def generateLabelforIF(self, valor):
        innerValue = ""
        if(valor == "true"):
            innerValue = f'IF_TRUE_{self.contadorGTrue}'
        elif(valor == "false"):
            innerValue = f'IF_FALSE_{self.contadorGTrue}'
            self.contadorGTrue += 1
        elif valor == 'endIf':
            innerValue = f'END_IF_{self.contadorGTrue}'
        else:
            innerValue = f'{valor}:'

        return innerValue

    def generateLabelforArray(self, var, temp):
        innerValue = ''
        if len(var) > 0:
            if(var["Scope"] == "GLOBAL"):
                innerValue = f'G[{(temp)}]'
            else:
                innerValue = f'fp[{(temp)}]'

        return innerValue

    def exitStatement_if(self, ctx: decafAlejandroV2Parser.Statement_ifContext):
        parent = ctx.parentCtx
        abuelito = parent.parentCtx
        # instanciamos nodo nuevo
        if len(ctx.block()) == 1:
            nodoState = NodoBooleano()
            nodoB = self.dictCodigoIntermedio[ctx.expr()]
            nodoS1 = self.dictCodigoIntermedio[ctx.getChild(4)]
            #B = self.visitar(ctx.expression())
            label = self.generateLabelforIF("true")
            nodoB.setTrue(label)
            if(len(nodoB.getCode().split("\n")) >= 2):
                valueTemporal = nodoB.getCode().split(
                    "\n")[2].split("=")[0].strip()
            else:
                if(len(nodoB.getCode().split("=")) != 0):
                    valueTemporal = nodoB.getCode().split("=")[0].strip()
                else:
                    valueTemporal = f't{self.contadorTemporales-1}'
            labelEndIF = self.generateLabelforIF("false")
            # labelEndIF = nuevaEtiqueta(labelEndIF)
            codigoAunado = nodoB.getCode() + '\n' + ('IF ' + f'{valueTemporal} > 0 '  f'GOTO {nodoB.getTrue()}') + '\n' +\
                ('GOTO ' + labelEndIF) + '\n' + self.generateLabelforIF(nodoB.getTrue()) + \
                '\n' + ' ' + nodoS1.getCode() + '\n' + self.generateLabelforIF(labelEndIF) + '\n'
        else:
            nodoState = NodoBooleano()
            nodoB = self.dictCodigoIntermedio[ctx.expr()]
            S1 = self.dictCodigoIntermedio[ctx.block()[0]]
            S2 = self.dictCodigoIntermedio[ctx.block()[1]]
            if(len(nodoB.getCode().split("\n")) >= 2):
                valueTemporal = nodoB.getCode().split(
                    "\n")[2].split("=")[0].strip()
            else:
                if(len(nodoB.getCode().split("=")) != 0):
                    valueTemporal = nodoB.getCode().split("=")[0].strip()
                else:
                    valueTemporal = f't{self.contadorTemporales-1}'
            endIf = self.generateLabelforIF('endIf')
            nodoB.setTrue(self.generateLabelforIF('true'))
            nodoB.setFalse(self.generateLabelforIF('false'))

            codigoAunado = nodoB.getCode() + '\n' + ('IF ' + f'{valueTemporal} > 0 GOTO {nodoB.getTrue()} \n') + \
                (f'GOTO {nodoB.getFalse()} \n') + self.generateLabelforIF(nodoB.getTrue()) + '\n '+" " + S1.getCode() + '\n ' + \
                (f' GOTO {endIf}') + '\n' + self.generateLabelforIF(nodoB.getFalse()
                                                                    ) + '\n ' + " " + S2.getCode() + '\n' + self.generateLabelforIF(endIf) + '\n '

        nodoState.setCode(codigoAunado)
        self.dictCodigoIntermedio[ctx] = nodoState
        if not isinstance(abuelito, decafAlejandroV2Parser.Statement_whileContext):
            self.arrayProduccionesTerminadas.append(codigoAunado)

    def exitStatement_while(self, ctx: decafAlejandroV2Parser.Statement_whileContext):
        """ hijos_tipo = [self.tipoNodo[i] for i in ctx.children if isinstance(
            i, decafAlejandroV2Parser.BlockContext)]
        if len(hijos_tipo) == 1:
            self.tipoNodo[ctx] = hijos_tipo.pop() """
        parent = ctx.parentCtx
        abuelito = parent.parentCtx
        # codigo para nodo Booleano
        nodoWhile = NodoBooleano()
        nodoB = self.dictCodigoIntermedio[ctx.expr()]
        nodoS1 = self.dictCodigoIntermedio[ctx.getChild(4)]

        lblInicioWhile = self.generateLabelforWhile('startwhile')
        nodoB.setTrue(self.generateLabelforWhile('true'))
        nodoB.setFalse(self.generateLabelforWhile('endwhile'))
        valueTemporal = ""
        if(len(nodoB.getCode().split("\n")) >= 2):
            valueTemporal = nodoB.getCode().split(
                "\n")[2].split("=")[0].strip()
        else:
            if(len(nodoB.getCode().split("=")) != 0):
                valueTemporal = nodoB.getCode().split("=")[0].strip()
            else:
                valueTemporal = f't{self.contadorTemporales-1}'
        codigoAunado = ' ' + lblInicioWhile + '\n  ' + nodoB.getCode() + '\n' +  \
            ('  IF ' + f'{valueTemporal} > 0 ' + f'GOTO {nodoB.getTrue()}') + '\n ' + \
            (f' GOTO {nodoB.getFalse()}') + '\n  ' + self.generateLabelforWhile(nodoB.getTrue()) + '\n ' + '  ' + nodoS1.getCode() + '\n  ' +\
            (f' GOTO {lblInicioWhile}') + '\n ' + \
            self.generateLabelforWhile(nodoB.getFalse())

        nodoWhile.setCode(codigoAunado)

        self.dictCodigoIntermedio[ctx] = nodoWhile
        if not isinstance(abuelito, decafAlejandroV2Parser.Statement_ifContext):
            self.arrayProduccionesTerminadas.append(codigoAunado)

    def exitStatement_return(self, ctx: decafAlejandroV2Parser.Statement_returnContext):
        # si es una suma y creamos un nodoo nuevo
        parent = ctx.parentCtx
        abuelito = parent.parentCtx
        nodoReturn = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        nodoExpr = self.dictCodigoIntermedio[ctx.expr()]
        codigoAunado = nodoExpr.getCode() + ('RETURN ' + nodoExpr.getAddress()) + '\n'
        nodoReturn.addCode(codigoAunado)
        if not isinstance(abuelito, decafAlejandroV2Parser.Statement_ifContext):
            self.arrayProduccionesTerminadas.append(codigoAunado)
        #self.tipoNodo[ctx] = self.tipoNodo[ctx.expr()]
        self.dictCodigoIntermedio[ctx] = nodoReturn

    def exitStatement_methodcall(self, ctx: decafAlejandroV2Parser.Statement_methodcallContext):
        parent = ctx.parentCtx
        abuelito = parent.parentCtx
        hijo = self.dictCodigoIntermedio[ctx.getChild(
            0)]
        if not isinstance(abuelito, decafAlejandroV2Parser.Statement_ifContext) and not isinstance(abuelito, decafAlejandroV2Parser.Statement_whileContext):
            self.arrayProduccionesTerminadas.append(hijo.getCode())
        self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]

        #self.tipoNodo[ctx] = self.tipoNodo[ctx.method_call()]

    def exitStatement_break(self, ctx: decafAlejandroV2Parser.Statement_breakContext):
        error = self.ChildrenHasError(ctx)
        if error:
            self.tipoNodo[ctx] = self.ERROR
            return

        self.tipoNodo[ctx] = self.VOID

    def exitStatement_assign(self, ctx: decafAlejandroV2Parser.Statement_assignContext):
        result_type = self.VOID
        parent = ctx.parentCtx
        abuelito = parent.parentCtx
        nodoI = self.dictCodigoIntermedio[ctx.location()]
        nodoE = self.dictCodigoIntermedio[ctx.expr()]
        # creamos un nuevo nodo
        nodoS = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        nombre = ''
        codigoAunado = ""
        # concatenamos codigo segun regla S.codigo = E.codigo ||
        if ctx.location().var_id():
            nombre = ctx.location().var_id().getText()
            variable2 = self.findVar(nombre)
            variable = variable2["Id"]
        elif ctx.location().array_id():
            nombre = ctx.location().array_id().ID().getText()
            variable2 = self.findVar(nombre)
            variable = variable2["Id"]

        if nodoI.getCode() != '' and nodoE.getCode() == '':
            codigoAunado = nodoI.getCode() + (' ' + nodoI.getAddress() +
                                              ' = ' + nodoE.getAddress())
        elif nodoI.getCode() != '' and nodoE.getCode() != '':
            codigoAunado = nodoI.getCode() + nodoE.getCode() + \
                (' ' + nodoI.getAddress() + ' = ' + nodoE.getAddress())
        else:
            codigoAunado = nodoE.getCode() + (' ' + self.generateTopeGet(variable) +
                                              " = " + nodoE.getAddress())
        # agregamos el codigo para ID
        nodoS.addCode(codigoAunado)

        # agregamos el dict de nodos globales
        self.dictCodigoIntermedio[ctx] = nodoS
        if not isinstance(abuelito, decafAlejandroV2Parser.Statement_ifContext) and not isinstance(abuelito, decafAlejandroV2Parser.Statement_whileContext):
            self.arrayProduccionesTerminadas.append(codigoAunado)
        # print(nodo.getNode())
        # # TODO verificar cuando hay que hacer append y cuando no
        self.tipoNodo[ctx] = result_type

    def exitExpr_location(self, ctx: decafAlejandroV2Parser.Expr_locationContext):
        self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]
        self.tipoNodo[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]

    def exitExpr_literal(self, ctx: decafAlejandroV2Parser.Expr_literalContext):
        self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]
        self.tipoNodo[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]

    def exitExpr_methodCall(self, ctx: decafAlejandroV2Parser.Expr_methodCallContext):
        self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]
        self.tipoNodo[ctx] = self.dictCodigoIntermedio[ctx.getChild(
            0)]

    def exitExpr_parentesis(self, ctx: decafAlejandroV2Parser.Expr_parentesisContext):
        NodoE1 = self.dictCodigoIntermedio[ctx.getChild(1)]
        # si es una suma y creamos un nodoo nuevo
        nodoParentesis = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        # por regla E.dir = E1.dir
        nodoParentesis.addAddress(NodoE1.getAddress())
        # agregamos el codigo al nodo de E.codigo = E1.codigo
        nodoParentesis.addCode(NodoE1.getCode())
        # agregamos el nodo a los nodos globales
        self.dictCodigoIntermedio[ctx] = nodoParentesis

    def exitExpr_menos(self, ctx: decafAlejandroV2Parser.Expr_menosContext):
        NodoE1 = self.dictCodigoIntermedio[ctx.getChild(1)]
        # si es una suma y creamos un nodoo nuevo
        menosNode = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        # creamos nueva temporal y la agregamos,
        #  por regla semántica E.dir = new Temp()
        innerTemporal = self.generateTemporal()
        menosNode.addAddress(innerTemporal)
        # anidamos codigo por la regla semantica
        # E.codigo = E1.codigo || gen(E.dir '=' 'menos' E1.dir)
        codigoAunado = NodoE1.getCode() + (menosNode.getAddress() + " =  MENOS " +
                                           NodoE1.getAddress()) + '\n'
        # agregamos el codigo al nodo de E
        menosNode.addCode(codigoAunado)
        # agregamos el nodo a los nodos globales
        self.dictCodigoIntermedio[ctx] = menosNode

    def exitExpr_negacion(self, ctx: decafAlejandroV2Parser.Expr_negacionContext):
        NodoE1 = self.dictCodigoIntermedio[ctx.getChild(1)]
        # si es una suma y creamos un nodoo nuevo
        menosNode = Nodo(self.contadorGlobalNodos)
        self.contadorGlobalNodos += 1
        # creamos nueva temporal y la agregamos,
        #  por regla semántica E.dir = new Temp()
        innerTemporal = self.generateTemporal()
        menosNode.addAddress(innerTemporal)
        # anidamos codigo por la regla semantica
        # E.codigo = E1.codigo || gen(E.dir '=' 'menos' E1.dir)
        codigoAunado = '\n' + NodoE1.getCode() + (menosNode.getAddress() + " =  NEGADO " +
                                                  NodoE1.getAddress()) + '\n'
        # agregamos el codigo al nodo de E
        menosNode.addCode(codigoAunado)
        # agregamos el nodo a los nodos globales
        self.dictCodigoIntermedio[ctx] = menosNode

    def exitExpr_normal(self, ctx: decafAlejandroV2Parser.Expr_normalContext):
        if ctx.eq_op() is not None:
            # si es una operacion de equal
            nuevaTemporal = self.generateTemporal()
            nodoEqual = NodoBooleano()
            nodoConData = self.dictCodigoIntermedio[ctx.getChild(0)]
            nodoConData2 = self.dictCodigoIntermedio[ctx.getChild(2)]
            codigoAunado = nodoConData.getCode() + " " + nodoConData2.getCode() + " " + nuevaTemporal + " = " + nodoConData.getAddress() + " " + ctx.eq_op().getText() + " " + \
                nodoConData2.getAddress()
            nodoEqual.setCode(codigoAunado)
            self.dictCodigoIntermedio[ctx] = nodoEqual
        elif ctx.rel_op() is not None:
            # si es una operacion de de relacion
            nuevaTemporal = self.generateTemporal()
            nodoRel = NodoBooleano()
            nodoConData = self.dictCodigoIntermedio[ctx.getChild(0)]
            nodoConData2 = self.dictCodigoIntermedio[ctx.getChild(2)]
            codigoAunado = nodoConData.getCode() + " " + nodoConData2.getCode() + " " + nuevaTemporal + " = " + nodoConData.getAddress() + " " + ctx.rel_op().getText() + " " + \
                nodoConData2.getAddress()
            nodoRel.setCode(codigoAunado)
            self.dictCodigoIntermedio[ctx] = nodoRel
        elif ctx.cond_op() is not None:
            # si es una operacion de condOP
            nuevaTemporal = self.generateTemporal()
            nodoCond = NodoBooleano()
            valueTemporal1 = ""
            valueTemporal2 = ""
            nodoConData = self.dictCodigoIntermedio[ctx.getChild(0)]
            nodoConData2 = self.dictCodigoIntermedio[ctx.getChild(2)]
            if(ctx.cond_op().getText() == "&&" or ctx.cond_op().getText() == "||"):  # si es un AND
                if(len(nodoConData.getCode().split("\n")) >= 2):
                    valueTemporal1 = nodoConData.getCode().split(
                        "\n")[2].split("=")[0].strip()
                else:
                    if(len(nodoConData.getCode().split("=")) != 0):
                        valueTemporal1 = nodoConData.getCode().split("=")[
                            0].strip()
                    else:
                        valueTemporal1 = nodoConData.getCode().split("=")[0]

                if(len(nodoConData2.getCode().split("\n")) >= 2):
                    valueTemporal2 = nodoConData2.getCode().split(
                        "\n")[2].split("=")[0].strip()
                else:
                    if(len(nodoConData2.getCode().split("=")) != 0):
                        valueTemporal2 = nodoConData2.getCode().split("=")[
                            0].strip()
                    else:
                        valueTemporal2 = nodoConData2.getCode().split("=")[0]
                codigoAunado = nodoConData.getCode() + '\n' + nodoConData2.getCode() + '\n' + nuevaTemporal + " = " + \
                    f'{valueTemporal1}' + " " + \
                    ctx.cond_op().getText() + \
                    f' {valueTemporal2}'
                print("S")
            else:
                codigoAunado = nodoConData.getCode() + " " + nodoConData2.getCode() + " " + nuevaTemporal + " = " + nodoConData.getAddress() + " " + ctx.cond_op().getText() + " " + \
                    nodoConData2.getAddress()
            nodoCond.setCode(codigoAunado)
            self.dictCodigoIntermedio[ctx] = nodoCond
        else:
            self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
                0)]
        """ self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(
            0)] """

    def exitExpr_PrecedenciaMax(self, ctx: decafAlejandroV2Parser.Expr_PrecedenciaMaxContext):
        # si es una operacion aritmética
        NodoE1 = self.dictCodigoIntermedio[ctx.getChild(0)]
        NodoE2 = self.dictCodigoIntermedio[ctx.getChild(2)]
        if ctx.MULTIPLY() is not None:
            # si es una suma y creamos un nodoo nuevo
            sumaNode = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
            # creamos nueva temporal y la agregamos,
            #  por regla semántica E.dir = new Temp()
            innerTemporal = self.generateTemporal()
            sumaNode.addAddress(innerTemporal)
            # anidamos codigo por la regla semantica
            # E.codigo = E1.codigo || gen(E.dir '=' 'menos' E1.dir)
            codigoAunado = ' ' + NodoE1.getCode() + NodoE2.getCode() + (sumaNode.getAddress() + " = " +
                                                                        NodoE1.getAddress() + " * " + NodoE2.getAddress() + " ") + '\n'
            # agregamos el codigo al nodo de E
            sumaNode.addCode(codigoAunado)
            # agregamos el nodo a los nodos globales
            # agregamos el nodo a los nodos globales
            self.dictCodigoIntermedio[ctx] = sumaNode
        elif ctx.DIVIDE() is not None:
            # si es una suma y creamos un nodoo nuevo
            sumaNode = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
            # creamos nueva temporal y la agregamos,
            #  por regla semántica E.dir = new Temp()
            innerTemporal = self.generateTemporal()
            sumaNode.addAddress(innerTemporal)
            # anidamos codigo por la regla semantica
            # E.codigo = E1.codigo || gen(E.dir '=' 'menos' E1.dir)
            codigoAunado = ' ' + NodoE1.getCode() + NodoE2.getCode() + (sumaNode.getAddress() + " = " +
                                                                        NodoE1.getAddress() + " / " + NodoE2.getAddress() + " ") + '\n'
            # agregamos el codigo al nodo de E
            sumaNode.addCode(codigoAunado)
            # agregamos el nodo a los nodos globales
            self.dictCodigoIntermedio[ctx] = sumaNode
        elif ctx.REMINDER() is not None:
            # si es una suma y creamos un nodoo nuevo
            sumaNode = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
            # creamos nueva temporal y la agregamos,
            #  por regla semántica E.dir = new Temp()
            innerTemporal = self.generateTemporal()
            sumaNode.addAddress(innerTemporal)
            # anidamos codigo por la regla semantica
            # E.codigo = E1.codigo || gen(E.dir '=' 'menos' E1.dir)
            codigoAunado = ' ' + NodoE1.getCode() + NodoE2.getCode() + (sumaNode.getAddress() + " = " +
                                                                        NodoE1.getAddress() + " % " + NodoE2.getAddress() + " ") + '\n'
            # agregamos el codigo al nodo de E
            sumaNode.addCode(codigoAunado)
            # agregamos el nodo a los nodos globales
            self.dictCodigoIntermedio[ctx] = sumaNode

    def exitExpr_PrecedenciaMenor(self, ctx: decafAlejandroV2Parser.Expr_PrecedenciaMenorContext):
        # si es una operacion aritmética
        NodoE1 = self.dictCodigoIntermedio[ctx.getChild(0)]
        NodoE2 = self.dictCodigoIntermedio[ctx.getChild(2)]
        if ctx.ADD() is not None:
            # si es una suma y creamos un nodoo nuevo
            sumaNode = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
            # creamos nueva temporal y la agregamos,
            #  por regla semántica E.dir = new Temp()
            innerTemporal = self.generateTemporal()
            sumaNode.addAddress(innerTemporal)
            # anidamos codigo por la regla semantica
            # E.codigo = E1.codigo || gen(E.dir '=' 'menos' E1.dir)
            codigoAunado = ' ' + NodoE1.getCode() + NodoE2.getCode() + (sumaNode.getAddress() + " = " +
                                                                        NodoE1.getAddress() + " + " + NodoE2.getAddress() + " ") + '\n'
            # agregamos el codigo al nodo de E
            sumaNode.addCode(codigoAunado)
            # agregamos el nodo a los nodos globales
            # agregamos el nodo a los nodos globales
            self.dictCodigoIntermedio[ctx] = sumaNode
        elif ctx.SUB() is not None:
            # si es una suma y creamos un nodoo nuevo
            sumaNode = Nodo(self.contadorGlobalNodos)
            self.contadorGlobalNodos += 1
            # creamos nueva temporal y la agregamos,
            #  por regla semántica E.dir = new Temp()
            innerTemporal = self.generateTemporal()
            sumaNode.addAddress(innerTemporal)
            # anidamos codigo por la regla semantica
            # E.codigo = E1.codigo || gen(E.dir '=' 'menos' E1.dir)
            codigoAunado = ' ' + NodoE1.getCode() + NodoE2.getCode() + (sumaNode.getAddress() + " = " +
                                                                        NodoE1.getAddress() + " - " + NodoE2.getAddress() + " ") + '\n'
            # agregamos el codigo al nodo de E
            sumaNode.addCode(codigoAunado)
            # agregamos el nodo a los nodos globales
            self.dictCodigoIntermedio[ctx] = sumaNode

    def CheckErrorInArrayId(self, ctx, tipo, tipo_var):
        id = ctx.getChild(0).getText()
        # variable = self.findVar(id)
        # tipo = variable['Tipo']

        if ctx.int_literal() is not None:
            if 'array' in tipo:
                if tipo.split('array')[-1] in [self.INT, self.STRING, self.BOOLEAN]:
                    self.tipoNodo[ctx] = self.data_type[tipo.split(
                        'array')[-1]]
                else:
                    self.tipoNodo[ctx] = self.VOID
            else:
                line = ctx.start.line
                col = ctx.start.column
                self.errores.AddEntryToTable(
                    line, col, f'Variable "{id}" debe ser del tipo ARRAY.')
                self.tipoNodo[ctx] = self.ERROR
        elif ctx.var_id() is not None:
            # tipo_var = self.findVar(ctx.var_id().getText())

            if 'array' in tipo and tipo_var['Tipo'] == self.INT:
                if tipo.split('array')[-1] in [self.INT, self.STRING, self.BOOLEAN]:
                    self.tipoNodo[ctx] = self.data_type[tipo.split(
                        'array')[-1]]
                else:
                    self.tipoNodo[ctx] = self.VOID

    def IterateChildren(self, location, parent_type, description):
        if location.var_id() is not None:
            # CASO BASE
            if location.var_id().location() is None:
                tipo_retorno = self.ERROR
                id = location.var_id().getChild(0).getText()
                if description is None:
                    self.tipoNodo[location] = self.ERROR
                    # line = location.start.line
                    # col = location.start.column
                    # self.errores.AddEntryToTable(line, col, f'Variable "{id}" no ha sido declarada previamente.')
                else:
                    if 'struct' in description:
                        child = self.tabla_estructuras.getChild(
                            parent_type, id)
                        if child == 0:
                            self.tipoNodo[location] = self.ERROR
                            line = location.start.line
                            col = location.start.column
                            self.errores.AddEntryToTable(
                                line, col, f'Variable "{id}" no ha sido declarada previamente.')
                        else:
                            tipo_nodo = self.tablaVariables.getSymbolFromTable(
                                child['Tipo'])
                            tipo_retorno = tipo_nodo['Tipo']
                            self.tipoNodo[location] = tipo_nodo['Tipo']
                    else:
                        line = location.start.line
                        col = location.start.column
                        self.errores.AddEntryToTable(
                            line, col, self.errores.errrorText_ESTRUCTURAGENERAL)
                        self.tipoNodo[location] = self.ERROR

                return tipo_retorno

            id = location.var_id().getChild(0).getText()
            tipo_nodo = None
            child_type = None
            child_desc = None

            if description is None:
                line = location.start.line
                col = location.start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_ESTRUCTURAGENERAL)
            else:
                if 'struct' in description:
                    child = self.tabla_estructuras.getChild(parent_type, id)
                    if child == 0:
                        line = location.start.line
                        col = location.start.column
                        self.errores.AddEntryToTable(
                            line, col, f'Variable "{id}" no ha sido declarada previamente.')
                    else:
                        child_type = child['Tipo']
                        child_desc = child['Description']
                        tipo_nodo = self.tablaVariables.getSymbolFromTable(
                            child['Tipo'])
                else:
                    line = location.start.line
                    col = location.start.column
                    self.errores.AddEntryToTable(
                        line, col, self.errores.errrorText_ESTRUCTURAGENERAL)

            result_type = self.IterateChildren(
                location.var_id().location(), child_type, child_desc)
            self.tipoNodo[location] = result_type
            return result_type

        elif location.array_id() is not None:
            # CASO BASE

            if location.array_id().location() is None:
                tipo_retorno = self.ERROR
                id = location.array_id().getChild(0).getText()
                if description is None:
                    self.tipoNodo[location] = self.ERROR
                    # line = location.start.line
                    # col = location.start.column
                    # self.errores.AddEntryToTable(line, col, f'Variable "{id}" no ha sido declarada previamente.')
                else:
                    if 'struct' in description:
                        child = self.tabla_estructuras.getChild(
                            parent_type, id)
                        if child == 0:
                            self.tipoNodo[location] = self.ERROR
                            line = location.start.line
                            col = location.start.column
                            self.errores.AddEntryToTable(
                                line, col, f'Variable "{id}" no ha sido declarada previamente.')
                        else:
                            # HIJO IZQUIERDO
                            tipo_nodo = self.tablaVariables.getSymbolFromTable(
                                child['Tipo'])
                            tipo_retorno = tipo_nodo['Tipo'].split('array')[-1]

                            # HIJO DERECHO
                            if location.array_id().int_literal() is not None:
                                if 'array' not in child['Tipo']:
                                    line = location.array_id().start.line
                                    col = location.array_id().start.column
                                    self.errores.AddEntryToTable(
                                        line, col, f'Variable "{id}" debe ser del tipo ARRAY.')  # ATENCION
                                    self.tipoNodo[location] = self.ERROR
                                else:
                                    self.tipoNodo[location] = child['Tipo'].split(
                                        'array')[-1]
                            elif location.array_id().var_id() is not None:
                                tipo = child['Tipo']
                                tipo_var = self.findVar(
                                    location.array_id().var_id().getText())
                                self.CheckErrorInArrayId(
                                    location.array_id(), tipo, tipo_var)

                                if self.tipoNodo[location.array_id()] != self.ERROR:
                                    self.tipoNodo[location] = tipo_nodo['Tipo'].split(
                                        'array')[-1]
                                else:
                                    tipo_retorno = self.ERROR
                                    self.tipoNodo[location] = self.ERROR
                    else:
                        line = location.start.line
                        col = location.start.column
                        self.errores.AddEntryToTable(
                            line, col, self.errores.errrorText_ESTRUCTURAGENERAL)
                        self.tipoNodo[location] = self.ERROR
                return tipo_retorno

            id = location.array_id().getChild(0).getText()
            tipo_nodo = None
            child_type = None
            child_desc = None

            tipo_retorno = self.VOID
            if 'struct' in description:
                child = self.tabla_estructuras.getChild(parent_type, id)
                if child == 0:
                    line = location.start.line
                    col = location.start.column
                    self.errores.AddEntryToTable(
                        line, col, f'Variable "{id}" no ha sido declarada previamente.')
                else:
                    child_type = child['Tipo']
                    child_desc = child['Description']
                    # tipo_nodo = self.tablaVariables.getSymbolFromTable(child['Tipo'])

                    # HIJO IZQUIERDO
                    tipo_nodo = self.tablaVariables.getSymbolFromTable(
                        child['Tipo'])

                    # HIJO DERECHO
                    if location.array_id().int_literal() is not None:
                        if 'array' not in child['Tipo']:
                            line = location.array_id().start.line
                            col = location.array_id().start.column
                            self.errores.AddEntryToTable(
                                line, col, f'Variable "{id}" debe ser un array.')
                            self.tipoNodo[location] = self.ERROR
                    elif location.array_id().var_id() is not None:
                        tipo = child['Tipo']
                        tipo_var = self.findVar(
                            location.array_id().var_id().getText())
                        self.CheckErrorInArrayId(
                            location.array_id(), tipo, tipo_var)

                    if location.array_id() in self.tipoNodo.keys():
                        if self.tipoNodo[location.array_id()] == self.ERROR:
                            tipo_retorno = self.ERROR
                        # self.tipoNodo[location] = self.ERROR
            else:
                line = location.start.line
                col = location.start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_ESTRUCTURAGENERAL)

            result_type = self.IterateChildren(
                location.array_id().location(), child_type, child_desc)
            self.tipoNodo[location] = result_type
            if tipo_retorno == self.ERROR:
                self.tipoNodo[location] = tipo_retorno
                result_type = tipo_retorno
            return result_type

    def enterLocation(self, ctx: decafAlejandroV2Parser.LocationContext):

        if ctx in self.tipoNodo.keys():
            return
        if ctx.var_id() is not None:
            if ctx.var_id().location() is None:
                return
        elif ctx.array_id() is not None:
            if ctx.array_id().location() is None:
                return

        if ctx.var_id() is not None:
            if ctx.var_id().location() is not None:
                id = ctx.var_id().getChild(0).getText()
                # self.scope_Actual.valueToTable()

                symbol = self.findVar(id)
                if symbol == 0:
                    line = ctx.start.line
                    col = ctx.start.column
                    self.errores.AddEntryToTable(
                        line, col, f'Variable "{ctx.var_id().getChild(0).getText()}" no ha sido declarada previamente.')
                    self.tipoNodo[ctx] = self.ERROR
                else:
                    tipo_id = self.tablaVariables.getSymbolFromTable(
                        symbol['Tipo'])
                    print('Tipo de variable', tipo_id)
                    if 'array' in tipo_id['Tipo']:
                        line = ctx.start.line
                        col = ctx.start.column
                        self.errores.AddEntryToTable(
                            line, col, f'Variable "{ctx.var_id().getChild(0).getText()}" debe ser un del tipo ARRAY.')
                        self.tipoNodo[ctx] = self.ERROR
                        return
                    result_type = self.IterateChildren(
                        ctx.var_id().location(), tipo_id['Tipo'], tipo_id['Description'])
                    self.tipoNodo[ctx] = result_type

        if ctx.array_id() is not None:
            if ctx.array_id().location() is not None:
                id = ctx.array_id().getChild(0).getText()
                symbol = self.findVar(id)
                if symbol == 0:
                    line = ctx.start.line
                    col = ctx.start.column
                    self.errores.AddEntryToTable(
                        line, col, f'Variable "{ctx.array_id().getChild(0).getText()}" no ha sido declarada previamente.')
                    self.tipoNodo[ctx] = self.ERROR
                else:
                    tipo_id = self.tablaVariables.getSymbolFromTable(
                        symbol['Tipo'])
                    result_type = self.IterateChildren(
                        ctx.array_id().location(), tipo_id['Tipo'], tipo_id['Description'])
                    self.tipoNodo[ctx] = result_type

                # Hijo derecho
                    if ctx.array_id().int_literal() is not None:
                        if 'array' not in tipo_id['Tipo']:
                            line = ctx.array_id().start.line
                            col = ctx.array_id().start.column
                            self.errores.AddEntryToTable(
                                line, col, f'Variable "{id}" debe ser un array.')
                            self.tipoNodo[ctx] = self.ERROR
                    elif ctx.array_id().var_id() is not None:
                        tipo = tipo_id['Tipo']
                        tipo_var = self.findVar(
                            ctx.array_id().var_id().getText())
                        self.CheckErrorInArrayId(
                            ctx.array_id(), tipo, tipo_var)

                    if ctx.array_id() in self.tipoNodo.keys():
                        if self.tipoNodo[ctx.array_id()] == self.ERROR:
                            self.tipoNodo[ctx] = self.ERROR

    def exitLocation(self, ctx: decafAlejandroV2Parser.LocationContext):
        if(ctx not in self.dictCodigoIntermedio.keys()):
            self.dictCodigoIntermedio[ctx] = self.dictCodigoIntermedio[ctx.getChild(
                0)]
        """ if ctx not in self.tipoNodo.keys():
            self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)] """

    def exitDeclaration(self, ctx: decafAlejandroV2Parser.DeclarationContext):
        self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)]

    def exitProgram(self, ctx: decafAlejandroV2Parser.ProgramContext):
        main_method = self.tabla_metodos.getSymbolFromTable('main')
        if main_method != 0:
            if len(main_method['Parameters']) > 0:
                self.tipoNodo[ctx] = self.ERROR
                self.errores.AddEntryToTable(
                    0, 0, self.errores.errrorText_MAIN_NOT_EXHISTS)
            else:
                hasError = self.ChildrenHasError(ctx)
                if hasError:
                    self.tipoNodo[ctx] = self.ERROR
                else:
                    self.tipoNodo[ctx] = self.VOID
        else:
            self.tipoNodo[ctx] = self.ERROR
            self.errores.AddEntryToTable(
                0, 0, self.errores.errrorText_MAIN_NOT_EXHISTS)

        # mostramos el codigo terminado
        for x in self.arrayProduccionesTerminadas:
            print(x)
        filename = 'codigoIntermedioFinal'
        outfile = open(filename, 'wb')
        pickle.dump(self.arrayProduccionesTerminadas, outfile)
        outfile.close()

        print('----------> FIN PROGRAMA <--------------')
        self.tabla_metodos.valueToTableV2()
        """self.tabla_metodos.valueToTable()
        self.tabla_estructuras.valueToTable() """


class CompilarIntermedio():
    def __init__(self, url):
        self.printer = None
        input = FileStream(url)
        lexer = decafAlejandroV2Lexer(input)
        stream = CommonTokenStream(lexer)
        parser = decafAlejandroV2Parser(stream)
        self.errorFromAntlr = MyErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(self.errorFromAntlr)
        tree = parser.program()

        if not self.errorFromAntlr.getHasError():
            self.printer = DecafAlejandroPrinter()
            walker = ParseTreeWalker()
            walker.walk(self.printer, tree)

    def HasLexicalError(self):
        return self.errorFromAntlr.getHasError()


comp = CompilarIntermedio('Python3/programs/multiple_tests.decaf')
