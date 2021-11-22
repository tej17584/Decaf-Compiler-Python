"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: noviembre 2021
Programa: compiladorFinal.py
Propósito: Esta clase aloja la logica del compilador final
V 2.0
"""

from os import name
from mainSemantic import Compilar
from mainIntermedio import CompilarIntermedio
from ARMGenerator import *
import pickle
from pprint import pp, pprint
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


class Compilador_Final():

    def __init__(self) -> None:
        """
        Variables iniciales finales
        """
        self.codigoIntermedio = []
        self.metodosCodigoIntermedio = {}
        self.sizeMetodoActual = 0
        self.metodoActual = ""
        self.primerMetodo = ""
        self.readIntermediateCode()
        self.limpiarCodigo()
        self.headerPlaced = False
        # variables globales para los registros
        self.descriptorRegistros = {
            'R0': [],
            'R1': [],
            'R2': [],
            'R3': [],
            'R4': [],
            'R5': [],
            'R6': [],
            'R7': [],
            'R8': [],
            'R9': [],
            'R10': [],
        }
        # Descriptor de direccciones
        self.descriptorDirecciones = {}
        # algunos operandos
        self.bool_operands = {
            '<=': 'bge',
            '>=': 'ble',
            '!=': 'bne',
            '==': 'beq',
            '<': 'bgt',
            '>': 'blt',
        }
        self.iterarCodigoIntermedio()

    def readIntermediateCode(self):
        infile = open("codigoIntermedioFinal", 'rb')
        self.codigoIntermedio = pickle.load(infile)
        infile2 = open("codigoMetodos", 'rb')
        self.metodosCodigoIntermedio = pickle.load(infile2)

    def limpiarCodigo(self):
        arrayTripleta = []
        for tripleta in self.codigoIntermedio:
            cont = 0
            for x in tripleta:
                if x != ' ':
                    tripLimpia = tripleta[cont:len(tripleta)]
                    arrayTripleta.append(tripLimpia)
                    break
                cont += 1

        innerArray = []
        for x in arrayTripleta:
            if '\n' in x:
                arraySplit = x.split('\n')
                for y in arraySplit:
                    if y != '' and y != ' ' and y != '   ':
                        innerArray.append(y)
            else:
                innerArray.append(x)

        for i in range(len(innerArray)):
            valor = innerArray[i]
            cont = 0
            for j in valor:
                if j.isalpha():
                    innerArray[i] = valor[cont:len(valor)]
                    break
                cont += 1

        self.codigoIntermedio = innerArray

    def iterarCodigoIntermedio(self):
        print("X")
        codigoAssemblerFinal = ""
        # isntancia del ARMG generator
        generadorCodigoARM = ARGCodigoGenerador()
        for x in self.codigoIntermedio:
            # condicion cuando iniciamos la definicion o es un DEF main
            if ('DEF' in x) and ('END DEF' not in x):
                # significa que es una definicion
                nameFuncion = x.replace('DEF ', '')
                nameFuncion = nameFuncion.replace(':', '')
                self.metodoActual = nameFuncion
                # buscamos su size en el dict y ahora ya lo tenemos
                for llave, valor in self.metodosCodigoIntermedio.items():
                    if(llave == nameFuncion):
                        self.sizeMetodoActual = valor
                # ahora miramos si es un header GLOBAL o solo uno extra
                if(self.headerPlaced == False):  # no han puesto el header, primero método que nos topamos
                    # generamos el encabezado inicial
                    self.headerPlaced = True
                    self.primerMetodo = nameFuncion
                    codigoAssemblerFinal += generadorCodigoARM.construirEncabezado(
                        nameFuncion)
                    # alocamos el tamaño de la funcion
                    codigoAssemblerFinal += generadorCodigoARM.alocarEspacioMetodo(
                        self.sizeMetodoActual)
                else:
                    # si es una declaracion nueva aparte de la global
                    codigoAssemblerFinal += generadorCodigoARM.construirFuncionNueva(
                        nameFuncion)
                    # alocamos el tamaño de la funcion
                    codigoAssemblerFinal += generadorCodigoARM.alocarEspacioMetodo(
                        self.sizeMetodoActual)

            elif('END DEF' in x):
                pass
            else:  # de lo contrario es una tripleta
                # obtenemos los registros
                codigo, registros, elementos = self.getReg(x)
                codigoAssemblerFinal += codigo
                if('+' in x) or ('*' in x) or ('-' in x):  # si es una operacion x= a + b
                    if('+' in x):  # si es una suma
                        esLiteral = False
                        literal = None
                        try:
                            y = int(y)
                            esLiteral = True
                            literal = y
                        except:
                            pass
                        if(esLiteral == True):
                            codigoAssemblerFinal += generadorCodigoARM.construirSumaV2(
                                registros, literal)
                        else:
                            codigoAssemblerFinal += generadorCodigoARM.construirSuma(
                                registros)
                    if('*' in x):  # si es una suma
                        codigoAssemblerFinal += generadorCodigoARM.construirMultiplicacion(
                            registros)
                    if('-' in x):  # si es una suma
                        codigoAssemblerFinal += generadorCodigoARM.construirResta(
                            registros)
                    # actualizamos
                    self.descriptorRegistros[registros[0]] = [elementos[0]]
                    self.descriptorDirecciones[elementos[0]] = [registros[0]]
                    for llave, valor in self.descriptorDirecciones.items():
                        if registros[0] in valor and llave != elementos[0]:
                            indice = valor.index(registros[0])
                            self.descriptorDirecciones[llave].pop(indice)

        print("-------------CODIGO ASSEMBLER FINAL----------")
        print()
        filename = 'codigoARMDumpPicke'
        outfile = open(filename, 'wb')
        pickle.dump(codigoAssemblerFinal, outfile)
        outfile.close()
        print(codigoAssemblerFinal)

    def getPositionSP(self, variable):
        if variable[0] == "f":  # es una variable Local
            val = str(variable[3:-1])
            if val.isnumeric():
                inst = f'[sp, #{val}]'
                return inst
            else:
                return variable
        else:
            return ""

    def getReg(self, tripletaEntrada):
        tripletaEntrada = str(tripletaEntrada).strip().replace(
            "\t", "").replace(" ", "")
        isOperation = False
        valueOperacion = ""
        arrayOperadores = ['+', '-', '*', '/', '%']
        codigoReturn = ""
        registros = ['', '', '']
        caso3 = False
        elements = []
        # Verificar si es una operacion u asignacion
        for x in arrayOperadores:
            if x in tripletaEntrada:
                isOperation = True
                valueOperacion = x

        llaves = self.descriptorDirecciones.keys()

        if isOperation:  # si la instruccion es tripleta
            pos_eq = tripletaEntrada.find("=")
            pos_op = tripletaEntrada.find(valueOperacion)
            x = tripletaEntrada[:pos_eq]
            y = tripletaEntrada[pos_eq+1:pos_op]
            z = tripletaEntrada[pos_op+1:]
            if x not in llaves:
                self.descriptorDirecciones[x] = [] if 't' in x else [x]
            if y not in llaves:
                self.descriptorDirecciones[y] = [] if 't' in y else [y]
            if z not in llaves:
                self.descriptorDirecciones[z] = [] if 't' in z else [z]
            print("Val1 ", x)
            print("Val2 ", y)
            print("Val3 ", z)
            elements = [x, y, z]
            caso3 = True
            # valor y
            # Revision de caso 1 y 2
            for llave, valor in self.descriptorRegistros.items():
                if y in valor:
                    print("Entro al caso 1, no se hace nada")
                    print("Reg ", llave)
                    registros[1] = llave
                    caso3 = False
                    break
                if y not in valor:
                    if len(valor) == 0:
                        print("Reg ", llave)
                        self.descriptorRegistros[llave] = [
                            y]  # se ingresa al registro
                        self.descriptorDirecciones[y].append(llave)
                        esLiteral = False
                        try:
                            y = int(y)
                            esLiteral = True
                        except:
                            pass
                        if(esLiteral == False):
                            codigoReturn += f"\tldr {llave}, {self.getPositionSP(y)}\n"
                        else:
                            codigoReturn += f"\tmov {llave}, #{y}\n"
                            codigoReturn += f"\tstr {llave}, [sp]\n"
                        registros[1] = llave
                        caso3 = False
                        break
            if caso3:  # No encontro primeros casos
                for llave, valor in self.descriptorDirecciones.items():
                    # ingresar casos de caso 3
                    if len(valor) > 1:
                        index = 0
                        for val in valor:
                            if 'R' in val:
                                break
                            index += 1
                        tempR = self.descriptorDirecciones[llave].pop(
                            index)  # se quita el registro
                        self.descriptorRegistros[tempR] = llave
                        esLiteral = False
                        try:
                            y = int(y)
                            esLiteral = True
                        except:
                            pass
                        if(esLiteral == False):
                            codigoReturn += f"\tldr {tempR}, {self.getPositionSP(y)}\n"
                        else:
                            codigoReturn += f"\tmov {tempR}, #{y}\n"
                            codigoReturn += f"\tstr {tempR}, [sp]\n"
                        registros[1] = llave
                        break

            caso3 = True
            # valor z Revision de caso 1 y 2
            for llave, valor in self.descriptorRegistros.items():
                if z in valor:
                    print("Entro al caso 1, no se hace nada")
                    print("Reg ", llave)
                    registros[2] = llave
                    caso3 = False
                    break
                if z not in valor:
                    if len(valor) == 0:
                        print("Reg ", llave)
                        self.descriptorRegistros[llave] = [
                            z]  # se ingresa al registro
                        self.descriptorDirecciones[z].append(llave)
                        esLiteral = False
                        try:
                            z = int(z)
                            esLiteral = True
                        except:
                            pass
                        if(esLiteral == False):
                            codigoReturn += f"\tldr {llave}, {self.getPositionSP(z)}\n"
                        else:
                            codigoReturn += f"\tmov {llave}, #{z}\n"
                            codigoReturn += f"\tstr {llave}, [sp]\n"
                        registros[2] = llave
                        caso3 = False
                        break
            if caso3:  # no se encontro nada en los otros casos
                for llave, valor in self.descriptorDirecciones.items():
                    # ingresar casos de caso 3
                    if len(valor) > 1:
                        index = 0
                        for val in valor:
                            if 'R' in val:
                                break
                            index += 1
                        tempR = self.descriptorDirecciones[llave].pop(
                            index)  # se quita el registro
                        self.descriptorRegistros[tempR] = llave
                        esLiteral = False
                        try:
                            z = int(z)
                            esLiteral = True
                        except:
                            pass
                        if(esLiteral == False):
                            codigoReturn += f"\tldr {tempR}, {self.getPositionSP(z)}\n"
                        else:
                            codigoReturn += f"\tmov {tempR}, #{z}\n"
                            codigoReturn += f"\tstr {tempR}, [sp]\n"
                        registros[2] = llave
                        break

            # valor x
            for llave, valor in self.descriptorRegistros.items():  # Caso 1
                if x in valor:
                    registros[0] = llave
                    break

            if registros[0] == '':  # No se cumple el caso 1
                registros[0] = registros[1]

            self.descriptorDirecciones[x].append(registros[0])
            self.descriptorRegistros[registros[0]] = [x]

        else:  # si la instruccion es una asignacion
            pos_eq = tripletaEntrada.find("=")
            x = tripletaEntrada[:pos_eq]
            y = tripletaEntrada[pos_eq+1:]
            elements = [x, y]
            keysDir = self.descriptorDirecciones.keys()
            if x not in keysDir:
                self.descriptorDirecciones[x] = [] if 't' in x else [x]
            if y not in keysDir:
                self.descriptorDirecciones[y] = [] if 't' in y else [y]
            print("Val1 ", x)
            print("Val2 ", y)
            tempReg = self.descriptorDirecciones[y]
            regy = ""
            # Encontrar registro de Y
            for ele in tempReg:
                if "R" == ele[0]:
                    regy = ele

            # Agregar x al descriptor de registro Ry
            self.descriptorRegistros[regy].append(x)
            self.descriptorDirecciones[x] = [x]
            registros[0] = regy
            registros[1] = regy
            esLiteral = False
            try:
                x = int(x)
                esLiteral = True
            except:
                pass
            if(esLiteral == False):
                codigoReturn = f"\tstr {regy}, {self.getPositionSP(x)}\n"
            else:
                codigoReturn += f"\tmov {regy}, #{x}\n"
                codigoReturn += f"\tstr {regy}, [sp]\n"
        return codigoReturn, registros, elements



