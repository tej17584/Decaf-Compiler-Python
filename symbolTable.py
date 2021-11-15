"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: septiembre 2021
Programa: tablaSimbolosv2.py
Propósito: Este programa alojará 3 clases para cada tabla. Este es una nueva version del codigo
de las tablas de símbolos.
V 2.0
"""
# zona de imports
from prettytable import PrettyTable
from antlr4.tree.Tree import Tree
from funciones import *
import sys
import json


class generalSymbolTable():
    def __init__(self):
        """
        Init de los métodos de la tabla de simbolos
        """
        self.dictSimbolos = []  # diccionario para los simbolos
        self.offsetVariables = 0  # ofsset de variables y de valores
        self.pretty_table = PrettyTable()  # instancia de pretty table

        #print(' -- Nuevo SCOPE --')

    def AddEntryToTable(self, typeValue, idValue, size, offset, isParameter):
        """
        Agrega un valor a la tabla de simbolos general
        *@param: typeValue: el tipo de valor
        *@param: scope: el valor del id
        *@param: size: el size de ese valor
        *@param: offset: el offset de ese valor
        *@param: isParameter: bool para el parametro
        """
        self.dictSimbolos.append({'Tipo': typeValue, 'Id': idValue, 'Size': size, 'Offset': offset, 'IsParameter': isParameter
                                  })
        self.offsetVariables += size

    def getSymbolFromTable(self, variable):
        """
        Retorna el valor pasado o 0
        *@param: variable: el id del valor
        """
        innerArray = self.dictSimbolos.copy()
        innerArray.reverse()
        for symbol in innerArray:
            if symbol['Id'] == variable:
                return symbol

        return 0

    def getSize(self):
        """
        Retorna el tamaño de la tabla
        """
        return sum(symbol['Size'] for symbol in self.dictSimbolos)

    def valueToTable(self):
        """
        transforma un array o valor a tabla
        """
        self.pretty_table.field_names = [
            'Tipo', 'ID', 'Size', 'Offset', 'IsParameter']
        for i in self.dictSimbolos:
            self.pretty_table.add_row(list(i.values()))

        print(' --- Tabla simbolos generales ---')
        print(self.pretty_table)
        self.pretty_table.clear_rows()


class generalSymbolTableV2():
    def __init__(self):
        """
        Init de los métodos de la tabla de simbolos
        """
        self.dictSimbolos = []  # diccionario para los simbolos
        self.offsetVariables = 0  # ofsset de variables y de valores
        self.pretty_table = PrettyTable()  # instancia de pretty table

        #print(' -- Nuevo SCOPE --')

    def AddEntryToTable(self, typeValue, idValue, size, offset, isParameter, scope):
        """
        Agrega un valor a la tabla de simbolos general
        *@param: typeValue: el tipo de valor
        *@param: scope: el valor del id
        *@param: size: el size de ese valor
        *@param: offset: el offset de ese valor
        *@param: isParameter: bool para el parametro
        """
        self.dictSimbolos.append({'Tipo': typeValue, 'Id': idValue, 'Size': size, 'Offset': offset, 'IsParameter': isParameter, "Scope": scope
                                  })
        self.offsetVariables += size

    def getSymbolFromTable(self, variable):
        """
        Retorna el valor pasado o 0
        *@param: variable: el id del valor
        """
        innerArray = self.dictSimbolos.copy()
        innerArray.reverse()
        for symbol in innerArray:
            if symbol['Id'] == variable:
                return symbol

        return 0

    def getSize(self):
        """
        Retorna el tamaño de la tabla
        """
        return sum(symbol['Size'] for symbol in self.dictSimbolos)

    def valueToTable(self):
        """
        transforma un array o valor a tabla
        """
        self.pretty_table.field_names = [
            'Tipo', 'ID', 'Size', 'Offset', 'IsParameter', "Scope"]
        for i in self.dictSimbolos:
            self.pretty_table.add_row(list(i.values()))

        print(' --- Tabla simbolos generales ---')
        print(self.pretty_table)
        self.pretty_table.clear_rows()


class tableDictParameters():
    def __init__(self):
        """
        Init de la tabla de parámetros
        """
        self.pretty_table = PrettyTable()
        self.dictSimbolos = []
        #print(' -- INICIANDO NUEVO AMBITO --')

    def AddEntryToTable(self, typeValue, idValue):
        """
        Agregamos una entrada a la tabla de parámetros
        *@param: typeValue: el tipo de valor
        *@param: idValue: el id del valor
        """
        self.dictSimbolos.append({
            'Tipo': typeValue,
            'Id': idValue,
        })

    def getSymbolFromTable(self, variable):
        """
        Retorna el valor pasado
        *@param: variable: el id del valor
        """
        innerArray = self.dictSimbolos.copy()
        innerArray.reverse()
        for symbol in innerArray:
            if symbol['Id'] == variable:
                return symbol
        return 0

    def valueToTable(self):
        """
        transforma un array o valor a tabla
        """
        self.pretty_table.field_names = ['Tipo', 'ID']
        for i in self.dictSimbolos:
            self.pretty_table.add_row(list(i.values()))

        print(' --- Tabla parámetros ---')
        print(self.pretty_table)
        self.pretty_table.clear_rows()

    def cleanTable(self):
        """
        limpia una tabla, en este caso el dict de simbolos
        """
        self.valueToTable()
        self.dictSimbolos = []


class dictTableStruct():
    def __init__(self):
        """
        init d ela tabla de estructuras
        """
        self.pretty_table = PrettyTable()
        self.dictSimbolos = []

    def AddEntryToTable(self, parent, typeValue, idValue, description):
        """
        Agrega un nuevo valor de estructura
        *@param: parent: el padre de la struct
        *@param: typeValue: el tipo
        *@param: idValue: el id del valor
        *@param: description: la descripcion o valor
        """
        self.dictSimbolos.append({
            'Parent': parent,
            'Tipo': typeValue,
            'Id': idValue,
            'Description': description
        })

    def getSymbolFromTable(self, variable):
        """
        Retorna el valor pasado
        *@param: variable: el id del valor
        """
        innerArray = self.dictSimbolos.copy()
        innerArray.reverse()
        for symbol in innerArray:
            if symbol['Id'] == variable:
                return symbol
        return 0

    def valueToTable(self):
        """
        transforma un array o valor a tabla
        """
        self.pretty_table.field_names = ['Parent', 'Tipo', 'ID', 'Description']
        for i in self.dictSimbolos:
            self.pretty_table.add_row(list(i.values()))

        print(' --- Diccionario estructuras ---')
        print(self.pretty_table)
        self.pretty_table.clear_rows()

    def ExtractInfo(self, parent, scope, tabla_tipo):
        """
        Retorna el valor de informacion de la estructura y lo guarda en la tabla
        *@param: parent: el padre
        *@param: scope: el scope o lugar
        *@param: tabla_tipo: el tipo de tabla
        """
        for i in scope.dictSimbolos:
            typeValue = tabla_tipo.getSymbolFromTable(i['Tipo'])
            self.AddEntryToTable(
                parent, i['Tipo'], i['Id'], typeValue['Description'])

    def getChild(self, typeValue, name):
        """
        retorna el hijo
        *@param: typeValue:el tipo de valor
        *@param: scnameope: eel nombre
        """
        copy_symbols = self.dictSimbolos.copy()
        copy_symbols.reverse()
        for symbol in copy_symbols:
            if symbol['Parent'] in typeValue and symbol['Id'] == name:
                return symbol

        return 0


class dictTableMetods():
    def __init__(self):
        """
        init de la tabla de métodos
        """
        self.pretty_table = PrettyTable()
        self.arrayMetodos = []
        #print(' -- Nuevo SCOPE --')

    def AddEntryToTable(self, typeValue, idValue, parameters, returnVariable):
        """
        agrega un valor a la tabla
        *@param: typeValue: el tipo de método
        *@param: idValue: el ID
        *@param: parameters: los parametros si posee
        *@param: returnVariable: la variable de retorno si tiene
        """
        self.arrayMetodos.append({
            'Tipo': typeValue,
            'Id': idValue,
            'Parameters': parameters,
            'Return': returnVariable
        })

    def getSymbolFromTable(self, variable):
        """
        Retorna el valor pasado
        *@param: variable: el id del valor
        """
        for metodo in self.arrayMetodos:
            if metodo['Id'] == variable:
                return metodo

        return 0

    def valueToTable(self):
        """
        transforma un array o valor a tabla
        """
        self.pretty_table.field_names = ['Tipo', 'ID', 'Parameters', 'Return']
        for i in self.arrayMetodos:
            self.pretty_table.add_row(list(i.values()))

        print(' --- Diccionario métodos ---')
        print(self.pretty_table)
        self.pretty_table.clear_rows()


class dictTableVars():
    def __init__(self):
        """
        Init de la tabla de variables
        """
        # enumerador de valores
        self.ARRAY = 'array'
        self.STRUCT = 'struct'
        self.PRIMITIVE = 'primitive'
        self.typesArray = []
        # agregamos esos valores a la tabla de entradas con el size de cada una
        self.AddEntryToTable('int', 4, self.PRIMITIVE)
        self.AddEntryToTable('char', 2, self.PRIMITIVE)
        self.AddEntryToTable('boolean', 1, self.PRIMITIVE)
        self.AddEntryToTable('void', 0, self.PRIMITIVE)
        #print(' -- Dictionario de Variables --')

    def AddEntryToTable(self, typeValue, size, description):
        """
        Retorna el valor pasado
        *@param: typeValue: el tipo
        *@param: size: el tamaño de la var
        *@param: description: la descripcion de la variable
        """
        self.typesArray.append({
            'Tipo': typeValue,
            'Size': size,
            'Description': description
        })

    def getSymbolFromTable(self, typeValue):
        """
        Retorna el valor pasado
        *@param: variable: el id del valor
        """
        innerArray = self.typesArray.copy()
        innerArray.reverse()
        for type in innerArray:
            if type['Tipo'] == typeValue:
                return type
        return 0
