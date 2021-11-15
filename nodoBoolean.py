"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: septiembre 2021
Programa: NodoBoolean.py
Propósito: Este programa aloja el nodo para el bool
V 2.0
"""


class NodoBooleano():

    def __init__(self) -> None:
        self.code = ""
        self.siguiente = ""
        self.trueValue = ""
        self.falseValue = ""
        self.address = ""

    def getCode(self):
        """
        Retorna el codigo del nodo
        """
        return self.code

    def setCode(self, codigo):
        """
        Agrega codigo al nodito
        *@param: codigo: el codigo a agregar al nodito
        """
        self.code = codigo

    def getSiguiente(self):
        """
        Retorna el siguiente
        """
        return self.siguiente

    def setSiguiente(self, next):
        """
        Agrega el next
        *@param: next: el next a agregar al nodito
        """
        self.code = next

    def getTrue(self):
        """
        Retorna el true
        """
        return self.trueValue

    def setTrue(self, value):
        """
        Agrega el true
        *@param: value: el nuevo valor
        """
        self.trueValue = value

    def getFalse(self):
        """
        Retorna el false
        """
        return self.falseValue

    def setFalse(self, value):
        """
        Agrega el false
        *@param: value: el nuevo valor false
        """
        self.falseValue = value

    def getAddress(self):
        """
        Retorna la direccion del nodo
        """
        return self.address

    def addAddress(self, address):
        """
        Agrega la direccion al nodito
        *@param: address: la address a agregar al nodito
        """
        self.address = address
