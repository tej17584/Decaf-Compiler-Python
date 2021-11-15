"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: septiembre 2021
Programa: mainSemantic.py
Propósito: Programa de nueva version del main anterior
V 2.0
"""

# ZONA DE IMPORTS
from decafAlejandroLexer import decafAlejandroLexer
from decafAlejandroParser import decafAlejandroParser
from decafAlejandroListener import decafAlejandroListener
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from funciones import *
from ErrorClass import *
from symbolTable import *
import emoji
import sys
from pprint import pprint
from itertools import groupby
from symbolTable import *
# we import Node
from NodoCodigo import *


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


class DecafAlejandroPrinter(decafAlejandroListener):
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
        self.tablaVariables = dictTableVars()
        self.errores = SemanticError()
        self.tabla_metodos = dictTableMetods()
        self.tabla_estructuras = dictTableStruct()
        self.tabla_parametros = tableDictParameters()

        self.dictNodosCodigoIntermedio = {}
        self.contadorNodos = 0

        self.tipoNodo = {}  # el tipo de nodo de cada valor que iteraremos

        super().__init__()

    def popScope(self):
        self.scope_Actual.valueToTable()
        self.scope_Actual = self.ambitos.pop()

    def addScope(self):
        self.ambitos.append(self.scope_Actual)
        self.scope_Actual = generalSymbolTable()

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
            i) in [decafAlejandroParser.LocationContext,
                   decafAlejandroParser.ExprContext,
                   decafAlejandroParser.BlockContext,
                   decafAlejandroParser.DeclarationContext]]
        if self.ERROR in non_terminals:
            return True
        return False

    def enterProgram(self, ctx: decafAlejandroParser.ProgramContext):
        print('----------> INICIO COMPILACION <--------------')
        self.root = ctx
        self.scope_Actual = generalSymbolTable()

    def enterMethod_declr(self, ctx: decafAlejandroParser.Method_declrContext):
        metodo = ctx.method_name().getText()
        parameters = []

        if self.tabla_metodos.getSymbolFromTable(metodo) == 0:
            if ctx.return_type().var_type() is not None:
                tipo = ctx.return_type().var_type().getText()
            else:
                tipo = ctx.return_type().getText()
            hijos = ctx.getChildCount()

            for i in range(hijos):
                if isinstance(ctx.getChild(i), decafAlejandroParser.Var_typeContext):
                    typeParameter = self.data_type[ctx.getChild(i).getText()]
                    idParameter = ctx.getChild(i + 1).getText()
                    if idParameter in [i['Id'] for i in parameters]:
                        line = ctx.getChild(i + 1).start.line
                        col = ctx.getChild(i + 1).start.column
                        self.errores.AddEntryToTable(
                            line, col, self.errores.errrorText_VARDUPLICADA)

                    parameters.append(
                        {'Tipo': typeParameter, 'Id': idParameter})
                    self.tabla_parametros.AddEntryToTable(
                        typeParameter, idParameter)

            self.tabla_metodos.AddEntryToTable(tipo, metodo, parameters, None)
        else:
            # self.tipoNodo
            line = ctx.method_name().start.line
            col = ctx.method_name().start.column
            self.errores.AddEntryToTable(
                line, col, self.errores.errrorText_VARDUPLICADA)

        self.addScope()

        for parameter in parameters:
            type_symbol = self.tablaVariables.getSymbolFromTable(
                parameter['Tipo'])
            size = type_symbol['Size']
            offset = self.scope_Actual.offsetVariables
            self.scope_Actual.AddEntryToTable(
                parameter['Tipo'], parameter['Id'], size, offset, True)

    def exitMethod_declr(self, ctx: decafAlejandroParser.Method_declrContext):
        metodo = ctx.method_name().getText()
        self.tabla_parametros.cleanTable()
        self.popScope()

        return_type = ctx.return_type().getText()
        block_type = self.tipoNodo[ctx.block()]

        if return_type == self.VOID and block_type != self.VOID and block_type != self.ERROR:
            self.tipoNodo[ctx] = self.ERROR
            line = ctx.return_type().start.line
            col = ctx.return_type().start.column
            self.errores.AddEntryToTable(
                line, col, self.errores.errrorText_TIPOVOID)
            return

        if return_type != block_type:
            if block_type == self.ERROR:
                self.tipoNodo[ctx] = self.ERROR
                return

            self.tipoNodo[ctx] = self.ERROR
            line = ctx.block().start.line
            col = ctx.block().start.column
            self.errores.AddEntryToTable(
                line, col, self.errores.errrorText_TIPO_RETORNO)

        self.tipoNodo[ctx] = self.VOID

    def enterVardeclr(self, ctx: decafAlejandroParser.VardeclrContext):
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
                    tipo, id, size, offset, False)
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
                    tipo_array, id, size, offset, False)

            else:
                self.tipoNodo[ctx] = self.ERROR
                self.tipoNodo[ctx.field_var()] = self.ERROR
                line = ctx.field_var().var_id().start.line
                col = ctx.field_var().var_id().start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_VARDUPLICADA)

    def enterStruct_declr(self, cstx: decafAlejandroParser.Struct_declrContext):
        self.addScope()

    def exitStruct_declr(self, ctx: decafAlejandroParser.Struct_declrContext):
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

    def enterVar_id(self, ctx: decafAlejandroParser.Var_idContext):
        parent = ctx.parentCtx
        if parent in self.tipoNodo.keys():
            self.tipoNodo[ctx] = self.tipoNodo[parent]

    def exitVar_id(self, ctx: decafAlejandroParser.Var_idContext):
        parent = ctx.parentCtx
        if parent in self.tipoNodo.keys() or ctx in self.tipoNodo.keys():
            return

        # if ctx.getChildCount() == 1:
        id = ctx.getText()
        variable = self.findVar(id)
        if variable == 0:
            line = ctx.start.line
            col = ctx.start.column
            self.errores.AddEntryToTable(
                line, col, f'Variable "{id}" no ha sido declarada previamente.')
            self.tipoNodo[ctx] = self.ERROR
        else:
            if variable['Tipo'] in [self.INT, self.STRING, self.BOOLEAN]:
                self.tipoNodo[ctx] = self.data_type[variable['Tipo']]
            else:
                self.tipoNodo[ctx] = self.VOID
        # else:

    def enterArray_id(self, ctx: decafAlejandroParser.Array_idContext):
        parent = ctx.parentCtx
        if parent in self.tipoNodo.keys():
            self.tipoNodo[ctx] = self.tipoNodo[parent]

    def exitArray_id(self, ctx: decafAlejandroParser.Array_idContext):
        parent = ctx.parentCtx
        if parent in self.tipoNodo.keys() or ctx in self.tipoNodo.keys():
            return

        id = ctx.getChild(0).getText()
        variable = self.findVar(id)
        if variable == 0:
            line = ctx.start.line
            col = ctx.start.column
            self.errores.AddEntryToTable(
                line, col, f'Variable "{id}" no ha sido declarada previamente.')
            self.tipoNodo[ctx] = self.ERROR
        else:
            tipo = variable['Tipo']
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
                tipo = variable['Tipo']
                tipo_var = self.findVar(ctx.var_id().getText())
                self.CheckErrorInArrayId(ctx, tipo, tipo_var)

    def exitVar_type(self, ctx: decafAlejandroParser.Var_typeContext):
        self.tipoNodo[ctx] = self.VOID

    def exitField_var(self, ctx: decafAlejandroParser.Field_varContext):
        if ctx not in self.tipoNodo.keys():
            if ctx.var_id() is not None:
                self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)]
            elif ctx.array_id() is not None:
                self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)]

    def enterField_declr(self, ctx: decafAlejandroParser.Field_declrContext):
        tipo = ctx.var_type().getText()

        for child in ctx.children:
            if not isinstance(child, TerminalNode) and isinstance(child, decafAlejandroParser.Field_varContext):
                id = child.var_id().getText()

                if self.scope_Actual.getSymbolFromTable(id) == 0:
                    type_symbol = self.tablaVariables.getSymbolFromTable(tipo)
                    size = type_symbol['Size']
                    offset = self.scope_Actual.offsetVariables

                    self.scope_Actual.AddEntryToTable(
                        tipo, id, size, offset, False)
                else:
                    self.tipoNodo[child] = self.ERROR
                    line = child.var_id().start.line
                    col = child.var_id().start.column
                    self.errores.AddEntryToTable(
                        line, col, self.errores.errrorText_VARDUPLICADA)

    def exitField_declr(self, ctx: decafAlejandroParser.Field_declrContext):
        self.tipoNodo[ctx] = self.VOID
        for child in ctx.children:
            if not isinstance(child, TerminalNode):
                if self.tipoNodo[child] == self.ERROR:
                    self.tipoNodo[ctx] = self.ERROR
                    break

    def exitVardeclr(self, ctx: decafAlejandroParser.VardeclrContext):
        self.tipoNodo[ctx] = self.VOID
        for child in ctx.children:
            if not isinstance(child, TerminalNode):
                if self.tipoNodo[child] == self.ERROR:
                    self.tipoNodo[ctx] = self.ERROR
                    break

    def exitString_literal(self, ctx: decafAlejandroParser.String_literalContext):
        self.tipoNodo[ctx] = self.STRING

    def exitInt_literal(self, ctx: decafAlejandroParser.Int_literalContext):
        self.tipoNodo[ctx] = self.INT

    def exitBool_literal(self, ctx: decafAlejandroParser.Bool_literalContext):
        self.tipoNodo[ctx] = self.BOOLEAN

    def exitLiteral(self, ctx: decafAlejandroParser.LiteralContext):
        self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)]

    def enterBlock(self, ctx: decafAlejandroParser.BlockContext):
        parent = ctx.parentCtx

        if not isinstance(parent, decafAlejandroParser.Method_declrContext):
            self.addScope()

    def exitBlock(self, ctx: decafAlejandroParser.BlockContext):
        parent = ctx.parentCtx

        if not isinstance(parent, decafAlejandroParser.Method_declrContext):
            self.popScope()

        for child in ctx.children:
            if not isinstance(child, TerminalNode):
                if self.tipoNodo[child] == self.ERROR:
                    self.tipoNodo[ctx] = self.ERROR
                    return

        hijos_tipo = [self.tipoNodo[i] for i in ctx.children if isinstance(
            i, decafAlejandroParser.StatementContext)]
        filtered = list(filter(lambda tipo: tipo != self.VOID, hijos_tipo))
        if len(filtered) == 0:
            self.tipoNodo[ctx] = self.VOID
            return

        if len(filtered) == 1:
            self.tipoNodo[ctx] = filtered.pop()
            return

        if self.all_equal(filtered):
            self.tipoNodo[ctx] = filtered.pop()
        else:
            self.tipoNodo[ctx] = self.ERROR

    def exitMethod_call(self, ctx: decafAlejandroParser.Method_callContext):
        name = ctx.method_name().getText()
        parameters = []

        for child in ctx.children:
            if isinstance(child, decafAlejandroParser.ExprContext):
                parameters.append(child)

        method_info = self.tabla_metodos.getSymbolFromTable(name)
        if method_info == 0:
            self.tipoNodo[ctx] = self.ERROR
            line = ctx.method_name().start.line
            col = ctx.method_name().start.column
            self.errores.AddEntryToTable(
                line, col, f'El método "{name}" no existe o no ha sido declarado antes del scope actual.')
            return

        if len(parameters) != len(method_info['Parameters']):
            self.tipoNodo[ctx] = self.ERROR
            line = ctx.method_name().start.line
            col = ctx.method_name().start.column
            self.errores.AddEntryToTable(
                line, col, self.errores.errrorText_CANTIDAD_PARAMETROS)
            return

        if len(parameters) == 0:
            self.tipoNodo[ctx] = method_info['Tipo']
            return

        hasError = False
        for i in range(len(parameters)):
            tipo_parametro = self.tipoNodo[parameters[i]]
            if tipo_parametro == self.ERROR:
                self.tipoNodo[ctx] = self.ERROR
                return

            tipo_metodo = method_info['Parameters'][i]['Tipo']

            if tipo_parametro != tipo_metodo:
                hasError = True

                line = parameters[i].start.line
                col = parameters[i].start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_TIPOMETODOS)

            if hasError:
                self.tipoNodo[ctx] = self.ERROR
            else:
                self.tipoNodo[ctx] = method_info['Tipo']

    def GetMethodType(self, ctx):
        nodo = ctx.parentCtx
        hijos = [str(type(i))
                 for i in nodo.children if not isinstance(i, TerminalNode)]
        while str(decafAlejandroParser.Return_typeContext) not in hijos:
            nodo = nodo.parentCtx
            hijos = [str(type(i))
                     for i in nodo.children if not isinstance(i, TerminalNode)]

        if nodo.return_type().var_type() is not None:
            return nodo.return_type().var_type().getText()
        else:
            return nodo.return_type().getText()

    def exitStatement_if(self, ctx: decafAlejandroParser.Statement_ifContext):
        error = self.ChildrenHasError(ctx)
        if error:
            self.tipoNodo[ctx] = self.ERROR
            return

        tipo_if = self.tipoNodo[ctx.expr()]

        if tipo_if != self.BOOLEAN:
            self.tipoNodo[ctx] = self.ERROR
            line = ctx.expr().start.line
            col = ctx.expr().start.column
            self.errores.AddEntryToTable(line, col, self.errores.errrorText_IF)
            return

        hijos_tipo = [i for i in ctx.children if isinstance(
            i, decafAlejandroParser.BlockContext)]
        tipo_return = self.GetMethodType(ctx)
        if len(hijos_tipo) == 1:
            hijo_1 = hijos_tipo.pop()
            if tipo_return == self.tipoNodo[hijo_1]:
                self.tipoNodo[ctx] = self.tipoNodo[hijo_1]
            else:
                self.tipoNodo[ctx] = self.ERROR
                line = hijo_1.start.line
                col = hijo_1.start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_TIPO_RETORNO)
        else:
            if self.tipoNodo[hijos_tipo[0]] != tipo_return and self.tipoNodo[hijos_tipo[1]] != tipo_return:
                self.tipoNodo[ctx] = self.ERROR
                line = hijos_tipo[0].start.line
                col = hijos_tipo[0].start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_TIPO_RETORNO)

                line = hijos_tipo[1].start.line
                col = hijos_tipo[1].start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_TIPO_RETORNO)
                return
            elif self.tipoNodo[hijos_tipo[0]] != tipo_return:
                self.tipoNodo[ctx] = self.ERROR
                line = hijos_tipo[0].start.line
                col = hijos_tipo[0].start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_TIPO_RETORNO)
                return
            elif self.tipoNodo[hijos_tipo[1]] != tipo_return:
                self.tipoNodo[ctx] = self.ERROR
                line = hijos_tipo[1].start.line
                col = hijos_tipo[1].start.column
                self.errores.AddEntryToTable(
                    line, col, self.errores.errrorText_TIPO_RETORNO)
                return

            if self.tipoNodo[hijos_tipo[0]] == self.tipoNodo[hijos_tipo[1]]:
                self.tipoNodo[ctx] = self.tipoNodo[hijos_tipo.pop()]
            else:
                self.tipoNodo[ctx] = self.ERROR

    def exitStatement_while(self, ctx: decafAlejandroParser.Statement_whileContext):
        error = self.ChildrenHasError(ctx)
        if error:
            self.tipoNodo[ctx] = self.ERROR
            return

        tipo_while = self.tipoNodo[ctx.expr()]

        if tipo_while != self.BOOLEAN:
            self.tipoNodo[ctx] = self.ERROR
            line = ctx.expr().start.line
            col = ctx.expr().start.column
            self.errores.AddEntryToTable(
                line, col, self.errores.errrorText_WHILE)
            return

        hijos_tipo = [self.tipoNodo[i] for i in ctx.children if isinstance(
            i, decafAlejandroParser.BlockContext)]
        if len(hijos_tipo) == 1:
            self.tipoNodo[ctx] = hijos_tipo.pop()

    def exitStatement_return(self, ctx: decafAlejandroParser.Statement_returnContext):
        error = self.ChildrenHasError(ctx)
        if error:
            self.tipoNodo[ctx] = self.ERROR
            return

        self.tipoNodo[ctx] = self.tipoNodo[ctx.expr()]

    def exitStatement_methodcall(self, ctx: decafAlejandroParser.Statement_methodcallContext):
        error = self.ChildrenHasError(ctx)
        if error:
            self.tipoNodo[ctx] = self.ERROR
            return

        self.tipoNodo[ctx] = self.tipoNodo[ctx.method_call()]

    def exitStatement_break(self, ctx: decafAlejandroParser.Statement_breakContext):
        error = self.ChildrenHasError(ctx)
        if error:
            self.tipoNodo[ctx] = self.ERROR
            return

        self.tipoNodo[ctx] = self.VOID

    def exitStatement_assign(self, ctx: decafAlejandroParser.Statement_assignContext):
        error = self.ChildrenHasError(ctx)
        if error:
            self.tipoNodo[ctx] = self.ERROR
            return

        left = self.tipoNodo[ctx.location()]
        right = self.tipoNodo[ctx.expr()]
        result_type = self.VOID

        if left != right:
            result_type = self.ERROR
            line = ctx.assign_op().start.line
            col = ctx.assign_op().start.column
            self.errores.AddEntryToTable(
                line, col, self.errores.errrorText_EQUALS)
        self.tipoNodo[ctx] = result_type

    def exitExpr(self, ctx: decafAlejandroParser.ExprContext):
        hasError = self.ChildrenHasError(ctx)
        # if hasError:
        #     self.tipoNodo[ctx] = self.ERROR
        #     return

        nodes_nonterminals = []
        for child in ctx.children:
            if not isinstance(child, TerminalNode):
                nodes_nonterminals.append(child)

        if len(nodes_nonterminals) == 1:
            non_terminal = nodes_nonterminals.pop()

            self.tipoNodo[ctx] = self.tipoNodo[non_terminal]
        # elif len(nodes_nonterminals) == 0:
        #     self.tipoNodo[ctx] = self.VOID
        else:
            tipo1 = self.tipoNodo[ctx.getChild(0)]
            tipo2 = self.tipoNodo[ctx.getChild(2)]

            if self.ERROR in [tipo1, tipo2]:
                self.tipoNodo[ctx] = self.ERROR
                return

            result_type = self.ERROR
            error = ''
            hasError = False

            if ctx.eq_op() is not None:
                if len(self.Intersection([tipo1, tipo2], [self.STRING, self.INT, self.BOOLEAN])) > 0 and tipo1 == tipo2:
                    result_type = self.BOOLEAN
                else:
                    hasError = True
                    line = ctx.getChild(0).start.line
                    col = ctx.getChild(0).start.column
                    error = self.errores.errrorText_EQ_OPS
            elif ctx.arith_op() is not None or ctx.rel_op() is not None:
                if tipo1 == self.INT and tipo2 == self.INT:
                    result_type = self.INT
                    if ctx.rel_op() is not None:
                        result_type = self.BOOLEAN
                    """ elif tipo1 == self.FLOAT and tipo2 == self.INT:
                    result_type = self.FLOAT
                    if ctx.rel_op() is not None:
                        result_type = self.BOOLEAN

                elif tipo1 == self.INT and tipo2 == self.FLOAT:
                    result_type = self.FLOAT
                    if ctx.rel_op() is not None:
                        result_type = self.BOOLEAN
                    """
                else:
                    hasError = True
                    if tipo1 != self.INT:
                        line = ctx.getChild(0).start.line
                        col = ctx.getChild(0).start.column
                    else:
                        line = ctx.getChild(2).start.line
                        col = ctx.getChild(2).start.column

                    if ctx.arith_op() is not None:
                        error = self.errores.errrorText_ARITMETICA
                    else:
                        error = self.errores.errrorText_REL_OP
            elif ctx.cond_op() is not None:
                if tipo1 == self.BOOLEAN and tipo2 == self.BOOLEAN:
                    result_type = self.BOOLEAN
                else:
                    hasError = True
                    if tipo1 != self.BOOLEAN:
                        line = ctx.getChild(0).start.line
                        col = ctx.getChild(0).start.column
                    else:
                        line = ctx.getChild(2).start.line
                        col = ctx.getChild(2).start.column

                    error = self.errores.errrorText_CONDICIONALES_GENERAL
            else:
                result_type = self.VOID

            if hasError:
                self.errores.AddEntryToTable(line, col, error)
            self.tipoNodo[ctx] = result_type

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
            if tipo_var == 0:
                line = ctx.start.line
                col = ctx.start.column
                self.errores.AddEntryToTable(
                    line, col, f'Variable "{ctx.var_id().getText()}" no ha sido declarada previamente.')
                self.tipoNodo[ctx] = self.ERROR
                return

            if 'array' in tipo and tipo_var['Tipo'] == self.INT:
                if tipo.split('array')[-1] in [self.INT, self.STRING, self.BOOLEAN]:
                    self.tipoNodo[ctx] = self.data_type[tipo.split(
                        'array')[-1]]
                else:
                    self.tipoNodo[ctx] = self.VOID
            elif 'array' in tipo and tipo_var['Tipo'] != self.INT:
                line = ctx.start.line
                col = ctx.start.column
                self.errores.AddEntryToTable(
                    line, col, f'Variable "{ctx.var_id().getText()}" debe ser INT para intetar acceder a un ARRAY.')
                self.tipoNodo[ctx] = self.ERROR
            elif 'array' not in tipo:
                line = ctx.start.line
                col = ctx.start.column
                self.errores.AddEntryToTable(
                    line, col, f'Variable "{id}" debe ser del tipo ARRAY.')
                self.tipoNodo[ctx] = self.ERROR
            elif tipo_var['Tipo'] != self.INT:
                line = ctx.start.line
                col = ctx.start.column
                self.errores.AddEntryToTable(
                    line, col, f'Variable "{ctx.var_id().getText()}" debe ser INT para intetar acceder a un ARRAY.')
                self.tipoNodo[ctx] = self.ERROR

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

    def enterLocation(self, ctx: decafAlejandroParser.LocationContext):
        parent = ctx.parentCtx
        if parent in self.tipoNodo.keys():
            if self.tipoNodo[parent] == self.ERROR:
                self.tipoNodo[ctx] = self.ERROR

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
                self.scope_Actual.valueToTable()

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

    def exitLocation(self, ctx: decafAlejandroParser.LocationContext):
        if ctx not in self.tipoNodo.keys():
            self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)]

    def exitDeclaration(self, ctx: decafAlejandroParser.DeclarationContext):
        self.tipoNodo[ctx] = self.tipoNodo[ctx.getChild(0)]

    def exitProgram(self, ctx: decafAlejandroParser.ProgramContext):
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

        print('----------> FIN PROGRAMA <--------------')
        self.scope_Actual.valueToTable()
        self.tabla_metodos.valueToTable()
        self.tabla_estructuras.valueToTable()


class Compilar():
    def __init__(self, url):
        self.printer = None
        input = FileStream(url)
        lexer = decafAlejandroLexer(input)
        stream = CommonTokenStream(lexer)
        parser = decafAlejandroParser(stream)
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


comp = Compilar('Python3/programs/multiple_tests.decaf')
