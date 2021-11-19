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
        # declaramos un diccionario para el descriptor de registro
        self.DescriptorRegistro = {}
        # declaramos un diccionario para el descriptor de accesos
        self.DescriptorAcceso = {}

    def actualizarCasoLDR(self, Registro, X_value):
        """
        Caso cuando queremos cargar un valor a una direccion de registro
        *@param Registro: el registro que vamos a usar
        *@param X_value: el valor a cargar en el registro
        """
        print(f'LD {Registro}, {X_value}')
        self.DescriptorRegistro[Registro] = [X_value]

        self.DescriptorAcceso[X_value].append(Registro)

    def actualizarCasoSTR(self, X_value, Registro):
        """
        Caso cuando queremos hacer storage de un valor
        *@param Registro: el registro que vamos a usar
        *@param X_value: el valor a cargar en el registro
        """
        print(f'ST {X_value}, {Registro}')
        self.eliminarVarRegister(X_value)
        # como es un valor igualitario, es ella misma siempre, la guardamos asi
        self.DescriptorAcceso[X_value] = [X_value]

    def actualizarMultipleST(self, Registro):
        """
        Cuando son multiples storage
        *@param Registro: el registro que vamos a usar
        """
        for var in self.DescriptorRegistro[Registro]:
            self.actualizarCasoSTR(var, Registro)

    def eliminarVarRegister(self, variable):
        """
        Eliminamos la variable de todos los registros
        *@param variable: la variable a eliminar
        """
        for key, valor in self.DescriptorRegistro.items():
            try:
                valor.remove(variable)
            except:
                continue

    def actualizarCasoOP(self, Registro, X_Value):
        """
        Caso de actualizacion general de casos, reasignamos los valores dinámicamente
        *@param Registro: el registro a reasignar
        *@param X_value: el valor a cambiar dinámicamente entre cosas
        """

        # el dict del descripto de acceso en la posicion del valor es el registro
        self.DescriptorAcceso[X_Value] = [Registro]
        # igual, el descriptor de registro en la posicion del registro es el valor
        self.DescriptorRegistro[Registro] = [X_Value]
        # itemamos el descriptor de acceso y removemos si el valor no coincide
        for x in self.DescriptorAcceso.keys():
            if (x == X_Value):
                continue
            try:
                self.DescriptorAcceso[x].remove(Registro)
            except:
                pass

    def actualizarCasoCopia(self, X_value, RegistroCopia):
        """
        Caso cuando es una igualdada lo que tenemos
        *@param RegistroCopia: el valor que appendeamos al diccionario
        *@param X_value: el valor a igualar
        """
        self.DescriptorRegistro[RegistroCopia].append(X_value)
        self.DescriptorRegistro[X_value] = [RegistroCopia]
        pass

    def buscarRegistroEnAcceso(self, var):
        """
        Esta funcion busca un registro en el descriptor de acceso, mediante una
        var
        *@param var: la variable a buscar
        """
        for x in self.DescriptorAcceso[var]:
            if (x.find('R') != -1):  # si logramos encontrar el registro
                return x

    def getRegistroVacio(self, dictRegistros=None):
        """
        Busca un registro libre
        *@param dictRegistros: el diccionario de registros
        """
        # si no encontramos registros hacemos una copia deep
        if (not dictRegistros):
            dictRegistros = copy.deepcopy(self.DescriptorRegistro)

        # dict Registros lo iteramos, si tiene len0, es porque esta bacío y podemos usarlo
        for llave, valor in dictRegistros.items():
            if (len(valor) == 0):
                return llave

    def eliminarTemporalVar(self, variable):
        """
        Crea un nuevo registro en el dict, pero sin variable
        *@param variable: eliminar esa temporal
        """
        innerDict = {}
        copiaDiccionario = copy.deepcopy(self.DescriptorRegistro.items())
        for llave, valor in copiaDiccionario:
            # intentamos tener un valor de remover para la llave
            try:
                innerDict[llave] = valor.remove(variable)
            except:
                continue
        return innerDict

    def getCountDictAccesRegister(self, itemToSearch):
        """
        Este método busca y cuenta una lista de registros en las que aparece
        nuestro parámetro enviado
        *@param itemToSearch: el item a buscar
        """
        innerArray = []
        for i in self.DescriptorAcceso[itemToSearch]:
            if (i.find('R') != -1):
                # si encontramosel registro lo appendeamos
                innerArray.append(i)
        # retornamos el registro
        return innerArray

    def iterarRegistrosCasiLibres(self, itemToSearch, arrayUsados):
        """
        El método itera sobre los registros que tienen un UNICO valor,
        si ese valor esta en OTRO itemToSearch, lo retorna.
        *@param itemToSearch: el registro para probar si existe
        *@param arrayUsados: registros usados
        """
        for llave, valor in itemToSearch.items():
            # si el value del item que buscamos es 1
            if len(valor) == 1:
                # accedemos a los registro que tenemos guardados
                conteoRegistros = self.getCountDictAccesRegister(valor[0])
                # Si es mayor a dos sinficia que esta en OTRO lugar
                if (len(conteoRegistros) > 2):
                    conteoRegistros.remove(llave)  # removemos la key
                    # si el registro encontrado ESTA en los usados
                    if conteoRegistros[0] in arrayUsados:
                        continue  # pasamos
                    # de lo contrario retornamos el valor del otro ITEM search
                    return conteoRegistros[0]

    def getRegMayorPrecedencia(self, itemToSearch, arrayUsados):
        """
        Retorna el itemToSearch con MENOS variables
        *@param itemToSearch: el itemToSearch para buscar
        *@param arrayUsados: registros arrayUsados
        """
        innerArray = sorted(
            itemToSearch.items(), key=lambda x: len(x[1]), reverse=False)

        for x in innerArray:
            # si no se encuentra entre los usados
            if x[0] not in arrayUsados:
                return x[0]  # lo retornamos

    def getRegistroMain(self, varToSearch, OperadorOpcional=None, arrayUsados=[]):
        """
        ESta funcion busca en los registros y nos retorna uno para buscar.
        REtorna un registro disponible
        *@param varToSearch: la variable para obtener el registros
        *@param OperadorOpcional: el operando que si se pasa como parametro, significa que es un operando
        *@param arrayUsados: el array de variables usadas
        """
        if (len(self.DescriptorAcceso[varToSearch]) > 0):
            # evaluar si en acceso[varToSearch] hay algun registro, si lo hay lo llamaremos R
            RegistroTemporal = self.buscarRegistroEnAcceso(varToSearch)
            if (RegistroTemporal):
                print(f'{varToSearch} -> Caso 1')
                return RegistroTemporal

        RegistroTemporal = self.getRegistroVacio()
        if(RegistroTemporal):  # Si hay algun registro libre, retornarlo
            print(f'{varToSearch} -> Caso 2')
            self.actualizarCasoLDR(RegistroTemporal, varToSearch)
            return RegistroTemporal

        registroTemp = None  # si no tenemos un registro disponible

        if (OperadorOpcional):  # si la variable es un operando
            # eliminamos de forma tempora a OperadorOpcional de los registros que lo contengan
            registroTemp = self.eliminarTemporalVar(OperadorOpcional)
        else:
            # de lo contrario, lo copiamos y usamos
            registroTemp = copy.deepcopy(self.DescriptorRegistro)

        # Si hay algun registro libre, retornarlo
        RegistroTemporal = self.getRegistroVacio(registroTemp)
        # si es un operador
        if(RegistroTemporal):
            if not RegistroTemporal in arrayUsados:
                print(f'{varToSearch} -> Caso 3')
                self.actualizarCasoLDR(RegistroTemporal, varToSearch)
                return RegistroTemporal

        """
        Acá iteramos sobre los registros que tengan de length 1, miramos si
        la variable esta en OTRO registro, y retornamos R de ser asi
        """
        RegistroTemporal = self.iterarRegistrosCasiLibres(
            registroTemp, arrayUsados)  # iteramos los registros casi libres
        if RegistroTemporal:
            print(f'{varToSearch} -> Caso 4')
            self.actualizarCasoLDR(RegistroTemporal, varToSearch)
            return RegistroTemporal

        """
        Evaluamos que registro tiene menos variables para liberar, pasamos
        cada variable que buscamos a su direccion de memoria y luego seleccionamos
        el registro
        """
        print(f'{varToSearch} -> Caso 5')
        RegistroTemporal = self.getRegMayorPrecedencia(
            registroTemp, arrayUsados)  # buscamos el registro de mayor precedencia
        # actualizamos los diccionarios
        self.actualizarMultipleST(RegistroTemporal)
        self.actualizarCasoLDR(RegistroTemporal, varToSearch)
        return RegistroTemporal

    def getReg(self, var1, var2, var3=None):
        """
        Esta funcion hace uso de getRegistroMain que es la logica detras de los casos distintos
        que podemos llegar a tener.
        las variables son los parametros
        """
        operador = None
        arrayInner = []

        if (var3 == None):
            if (var1 == var2):  # es una asignacion as que se necesita solo de un registro
                operador = var1
            registro = self.getRegistroMain(var2, operador, arrayInner)
            arrayInner.append(registro)
            arrayInner.append(registro)

        else:
            if (var1 == var3 or var1 == var2):  # de lo contrario es una operacion
                operador = var1
            # iteramos sobre las variables
            for x in [var1, var2, var3]:
                arrayInner.append(self.getRegistroMain(
                    x, operador, arrayInner))

        return arrayInner

    def debug(self):
        print('##################')
        print('Registro:')
        for key, item in self.DescriptorRegistro.items():
            print(f'{key}: {item}')

        print('\nAcceso:')
        for key, item in self.DescriptorAcceso.items():
            print(f'{key}: {item}')
        print('##################')

    def __repr__(self):
        return f""


d = DescriptorGlobal()
d.DescriptorRegistro = {
    'R1': ['u'],
    'R2': ['t'],
    'R3': ['u']
}

d.DescriptorAcceso = {
    'a': ['a'],
    'b': ['b'],
    'c': ['c'],
    'd': ['d'],
    't': ['R2'],
    'u': ['R1', 'R3'],
    'v': [],
}

# t = a - b
d.debug()
print('t = a - b')
print(d.getReg(var1='t', var2='a', var3='b'))
d.debug()
print()
