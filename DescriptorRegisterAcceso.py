"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: noviembre 2021
Programa: DescriptorRegisterAcceso.py
Propósito: Esta clase alojará el descriptor de registros y el descriptor de acceso
V 2.0
"""
import copy
import json
from typing import ItemsView


class DescriptorGlobal:

    def __init__(self) -> None:
        """
        variables Iniciales y globales acá
        """
        print("El descriptor general esta iniciandose....")
        self.DescriptorRegistro = { } # declaramos un diccionario para el descriptor de registro
        self.DescritproAcceso = {} #declaramos un diccionario para el descriptor de accesos
