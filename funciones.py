"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: agosto 2021
Programa: funciones.py
Propósito: ESte programa tiene funciones útiles
V 2.0
"""

# ZONA DE IMPORTS
import json


class funciones():
    """
    Clase con funciones especiales para todas las clases
    """

    def __init__(self) -> None:
        self.ANYSET = set([chr(char) for char in range(0, 256)])

    def get_ANYSET(self):
        """
        Retorna el set de ANYSET
        """
        return self.ANYSET

    def printPrettyDictionary(self, d, indent=0):
        """
        this function prints pretty the dictionary,
        extracted from: https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries
        """
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                self.printPrettyDictionary(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))

    def getDumpJson(self, dictionary):
        """
        Retorna el dump de un diccionario para ser impreso en formato JSON
        dictionary: el diccionario para ser droppeado
        """
        return json.dumps(dictionary, indent=2, default=str)

    def fromSetToOrd(self, setToOrd):
        """
        Esta funcion convierte un set con characteres a un set de ords
        *@param setToOrd: el set a ser convertido
        """
        newSet = set()
        for x in setToOrd:
            newSet.add(ord(x))
        return newSet

    def fromOrdToString(self, ordToString):
        """
        Esta funcion convierte un set de ords en strings
        *@param setToOrd: el set a ser convertido
        """
        newSet = set()
        for x in ordToString:
            newSet.add(chr(x))
        return newSet

    def fromSetToSTring(self, setToTransform):
        """
        Esta funcion convierte un set a un string concatenado
        *@param setToTransform: el set a convertir
        """
        nuevoString = ""
        for x in setToTransform:
            nuevoString += x

        return nuevoString

    def fromSetNumbersToSTring(self, setToTransform):
        """
        Esta funcion convierte un set a un string concatenado
        *@param setToTransform: el set a convertir
        """
        if(isinstance(setToTransform, int)):
            return str(setToTransform)
        else:
            nuevoString = ""
            for x in setToTransform:
                nuevoString += chr(x)

        return nuevoString

    def sortString(self, str):
        """
        Hace sort de un string
        extraido de: https://www.geeksforgeeks.org/sort-string-characters/
        *@param: str: el string hacer sort
        """
        str = ''.join(sorted(str))
        return str

    def unionTwoStrings(self, string1, string2):
        """
        Une dos strings. Elimina duplicados.
        *@param: string1: el string a unir
        *@param: string2: el string a sumarle
        """
        res = ""
        temp = string1
        for i in string2:
            if i not in temp:
                string1 += i

        return string1

    def checkIfIsInt(self, valor):
        """
        Chequea si un valor es numero o letra
        *@param: valor: el valor a testear
        """
        try:
            int(valor)
            return True
        except:
            return False

    def checkGeneraltype(self, valor, tipo):
        """
        Chequea si un valor es numero o letra
        *@param: valor: el valor a testear
        *@param: tipo: el tipo de variable
        """
        if("'" in valor):
            if(tipo == "string"):
                return isinstance(valor, str)
            else:
                return False
        else:
            if(tipo == "int"):
                return self.checkIfIsInt(valor)
            elif(tipo == "bool" or tipo == "boolean"):
                if(valor == "true" or valor == "false"):
                    return True
                else:
                    return False
            else:
                return False

    def hasReturnValue(self, contexto):
        """
        Chequea si el statement tiene valor de retorno o no
        *@param: contexto: el contexto
        """
        tieneValorRetorn = contexto.RETURN()
        if(tieneValorRetorn != None):
            return True
        else:
            return False

    def removeOperations(self, operacionPlana):
        """
        Remueve los operadores de una expresion y retorna un array con las variables o valores
        *@param: operacionPlana: la operacion plana
        """
        nuevoArray = []
        if("+" in operacionPlana):
            operacionPlana = operacionPlana.replace("+", " ")
        if("-" in operacionPlana):
            operacionPlana = operacionPlana.replace("-", " ")
        if("*" in operacionPlana):
            operacionPlana = operacionPlana.replace("*", " ")
        if("/" in operacionPlana):
            operacionPlana = operacionPlana.replace("/", " ")
        if("%" in operacionPlana):
            operacionPlana = operacionPlana.replace("%", " ")
        if("(" in operacionPlana):
            operacionPlana = operacionPlana.replace("(", " ")
        if(")" in operacionPlana):
            operacionPlana = operacionPlana.replace(")", " ")

        # ahora retornamos el nuevo array
        nuevoArray = operacionPlana.split(" ")
        return nuevoArray
