"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: septiembre 2021
Programa: NodoCodigo.py
Propósito: Este programa aloja el nodo que usaremos para codigo
V 2.0
"""


class Nodo():

    def __init__(self, numeroNodo) -> None:
        self.code = ""
        self.address = ""
        self.correlativo = numeroNodo

    def getCode(self):
        """
        Retorna el codigo del nodo
        """
        return self.code

    def addCode(self, codigo):
        """
        Agrega codigo al nodito
        *@param: codigo: el codigo a agregar al nodito
        """
        self.code = codigo

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
