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
        self.DescriptorAcceso = {}  # declaramos un diccionario para el descriptor de accesos

    def actualizarCasoLD(self, R, x):
        '''
            Caso LD R, x
        '''
        print(f'LD {R}, {x}')
        self.DescriptorRegistro[R] = [x]

        self.DescriptorAcceso[x].append(R)

    def eliminarVariableDeRegistro(self, variable):
        '''
            Se elimina variable de todos los
            registros

            Parametro:
            - variable: variable a eliminar

        '''
        for key, value in self.DescriptorRegistro.items():
            try:
                value.remove(variable)
            except:
                continue

    def actualizarCasoST(self, x, R):
        '''
            Caso ST x, R
        '''
        print(f'ST {x}, {R}')
        self.eliminarVariableDeRegistro(x)
        self.DescriptorAcceso[x] = [x]  # solo sería ella misma

    def actualizarMultipleST(self, R):
        for var in self.DescriptorRegistro[R]:
            self.actualizarCasoST(var, R)

    def actualizarCasoOP(self, Rx, x):
        '''
            Caso ADD Rx, Ry, Rz
            x = y + z
        '''
        self.DescriptorRegistro[Rx] = [x]
        self.DescriptorAcceso[x] = [Rx]

        for i in self.DescriptorAcceso.keys():
            if (i == x):
                continue
            try:
                self.DescriptorAcceso[i].remove(Rx)
            except:
                pass

    def actualizarCasoCopia(self, x, Ry):
        '''
            Caso x = y
        '''
        self.DescriptorRegistro[Ry].append(x)
        self.DescriptorRegistro[x] = [Ry]
        pass

    def buscarRegistroEnAcceso(self, variable):
        '''
            Funcion para buscar un registro en
            el acceso de una variable

            Parametros:
            - variable: variable a evaluar

            Return:
            - Registro o Nada si no hay un registro
        '''
        for i in self.DescriptorAcceso[variable]:
            if (i.find('R') != -1):
                return i

    def getRegistroVacio(self, registro=None):
        '''
            Funcion para obtener un registro libre

            Retorno:
            - R si hay registro libre, de lo contrario
            nada.
        '''
        if (not registro):
            registro = copy.deepcopy(self.DescriptorRegistro)

        for key, value in registro.items():
            if (len(value) == 0):
                return key

    def eliminarXTemp(self, variable):
        '''
            Crea un registro sin variable

            Parametro:
            - variable: variable a eliminar

            Retorno:
            - registro sin variable
        '''
        registroTemp = {}
        for key, value in copy.deepcopy(self.DescriptorRegistro.items()):
            try:
                registroTemp[key] = value.remove(variable)
            except:
                continue
        return registroTemp

    def getCantRegistrosEnAcceso(self, variable):
        '''
            Retorna la lista de registros en los
            que esta una variable

            Parametros:
            - variable: variable a evaluar

            Retorno:
            - <list> registros
        '''
        registros = []
        for i in self.DescriptorAcceso[variable]:
            if (i.find('R') != -1):
                registros.append(i)
        return registros

    def iterarRegistrosCasiLibres(self, registro, usados):
        '''
            Itera sobre los registros que solo
            tienen un valor, si esa variable
            esta en otro registro, retorna R.

            Parametros:
            - registro: registroTemp para iterar
            - usados: parametros usados si no se
            quieren repetir

            Retorno:
            - R si hay un registro que cumpla,
            de lo contrario nada.
        '''
        for key, value in registro.items():
            if len(value) == 1:
                registros = self.getCantRegistrosEnAcceso(value[0])

                if (len(registros) > 2):
                    registros.remove(key)
                    if registros[0] in usados:
                        continue
                    return registros[0]

    def getMejorRegistro(self, registro, usados):
        '''
            Funcion para evaluar que registro tiene
            menos variables para liberar.

            Parametros:
            - registro: registro temporal
            - usados: registros usados por
            si no se quieren repetir

            Retorno:
            - Registro con menos variables.
        '''
        registroSort = sorted(
            registro.items(), key=lambda x: len(x[1]), reverse=False)

        for i in registroSort:
            if i[0] not in usados:
                return i[0]

    def getRegAuxiliar(self, variable, x=None, usados=[]):
        '''
            Funcion auxiliar para obtener un registro

            Parametros:
            - variable: variable a obtener un registro.
            - x: si se pasa como parametro, significa
            que x es un operando.
            - usados: registros usados, si en dado caso
            no se quieren repetir.

            Retorno:
            - Registro disponible para variable.
        '''
        if (len(self.DescriptorAcceso[variable]) > 0):
            # evaluar si en acceso[variable]
            # hay algun registro, si lo hay
            # lo llamaremos R
            Rtemp = self.buscarRegistroEnAcceso(variable)
            if (Rtemp):
                print(f'{variable} -> Caso 1')
                return Rtemp

        # Si hay algun registro libre, retornarlo
        Rtemp = self.getRegistroVacio()
        if(Rtemp):
            print(f'{variable} -> Caso 2')
            self.actualizarCasoLD(Rtemp, variable)
            return Rtemp

        # cuando no hay registro disponible:

        registroTemp = None

        # Evaluar si x no es un operando
        if (x):
            # eliminar de forma temporal a x de los
            # registros que lo contengan
            registroTemp = self.eliminarXTemp(x)
        else:
            registroTemp = copy.deepcopy(self.DescriptorRegistro)

        # Si hay algun registro libre, retornarlo
        Rtemp = self.getRegistroVacio(registroTemp)
        if(Rtemp):
            if not Rtemp in usados:
                print(f'{variable} -> Caso 3')
                self.actualizarCasoLD(Rtemp, variable)
                return Rtemp

        # Iterar sobre los registros que solo tengan
        # un valor, identificar si esa variable esta
        # en otro registro, de ser ese el caso seleccionar
        # ese registro (R)
        Rtemp = self.iterarRegistrosCasiLibres(registroTemp, usados)
        if Rtemp:
            print(f'{variable} -> Caso 4')
            self.actualizarCasoLD(Rtemp, variable)
            return Rtemp

        # Evaluar que registro tiene menos variables para liberar
        # Pasar cada variable a su direccion de memoria y
        # seleccionar ese registro (R)
        print(f'{variable} -> Caso 5')
        Rtemp = self.getMejorRegistro(registroTemp, usados)
        self.actualizarMultipleST(Rtemp)
        self.actualizarCasoLD(Rtemp, variable)
        return Rtemp

    def getReg(self, x, y, z=None):
        '''
            Funcion principal para obtener
            los registros dado x, y, z.

            x = y + z
            x = y

            Parametros:
            - x,y,z: variables de una instruccion

            Retorno:
            - lista de registros de la forma [Rx, Ry, Rz]
        '''
        registros = []
        xOperando = None

        if (z == None):
            # sabemos que es asignacion
            # asi que solo necesitamos
            # 1 registro
            if (x == y):
                xOperando = x

            registro = self.getRegAuxiliar(y, xOperando, registros)
            registros.append(registro)
            registros.append(registro)

        else:
            # es una operacion de la
            # forma x = y + z

            if (x == y or x == z):
                xOperando = x

            for variable in [x, y, z]:
                registros.append(self.getRegAuxiliar(
                    variable, xOperando, registros))

        return registros

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
print(d.getReg(x='t', y='a', z='b'))
d.debug()
print()
