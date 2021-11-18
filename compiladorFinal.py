"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: noviembre 2021
Programa: compiladorFinal.py
Propósito: Esta clase aloja la logica del compilador final
V 2.0
"""

from mainSemantic import Compilar
from mainIntermedio import CompilarIntermedio
import pickle
from pprint import pp, pprint


class Compilador_Final():

    def __init__(self) -> None:

        self.codigoIntermedio = []
        self.readIntermediateCode()
        self.limpiarCodigo()

    def readIntermediateCode(self):
        infile = open("codigoIntermedioFinal", 'rb')
        self.codigoIntermedio = pickle.load(infile)

    def limpiarCodigo(self):
        array = []
        for tripleta in self.codigoIntermedio:
            cont = 0
            for i in tripleta:
                if i != ' ':
                    tripLimpia = tripleta[cont:len(tripleta)]
                    array.append(tripLimpia)
                    break
                cont += 1

        arrayFinal = []
        for pos in array:
            if '\n' in pos:
                arraySplit = pos.split('\n')
                for posi in arraySplit:
                    if posi != '' and posi != ' ' and posi != '   ':
                        arrayFinal.append(posi)

        for i in range(len(arrayFinal)):
            valor = arrayFinal[i]
            cont = 0
            for j in valor:
                if j.isalpha():
                    arrayFinal[i] = valor[cont:len(valor)]
                    break
                cont += 1

        self.codigoIntermedio = arrayFinal
        pprint(self.codigoIntermedio)


compiladorsito = Compilador_Final()
print()
print("-----------------------------")
