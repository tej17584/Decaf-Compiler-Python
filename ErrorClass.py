"""
Nombre: Alejandro Tejada
Curso: Diseño Compiladores
Fecha: agosto 2021
Programa: ErrorClass.py
Propósito: este programa maneja los errores que podemos chequear
           y los imprime en consola
V 1.0
"""


class Errores():
    """
    Esta clase se encarga de los errores que puedan surgir y que podamos
    manejar a nivel lógico sin necesidad de tabla de símbolos
    """

    def __init__(self, nombre="", columna="", linea="", tipo="") -> None:
        self.nombre = nombre
        self.columna = columna
        self.linea = linea
        self.tipo = tipo
        self.arrayErrores = []

    def checkArrayError(self, numero, isLetter):
        """
        Método general de chequeado de errores para arrays
        *@param numero: es el numero declarado en el array
        *@param isLetter: indica si estamos tanteando una letra
        """
        # Chequeo de regla semántica: num en la
        # declaración de un arreglo debe de ser mayor a 0.
        if(numero <= 0 and (isLetter == False)):
            return True, f'Error de declaración del array con nombre:{self.nombre}. En linea: {self.linea}, columna:{self.columna}. El valor declarado es de : -> {numero} <- y se espera uno mayor a 0'
        elif(numero <= 0 and (isLetter == True)):
            return True, f'Error de declaración del array con nombre:{self.nombre}. En linea: {self.linea}, columna:{self.columna}. La variable usada DENTRO del array tiene un valor de: -> {numero} <- y se espera uno mayor a 0'
        return False, ""

    def addNewError(self, error):
        """
        Método para agregar un nuevo error al stack
        *@param error: el nuevo error
        """
        self.arrayErrores.append("--> ", error)

    def getAllErrors(self):
        """
        REtorna todos los errores
        """
        return self.arrayErrores


class SemanticError():
    def __init__(self):
        self.errores = []
        self.errrorText_VARDUPLICADA = 'No se puede tener un identificador declarado DOS veces en el mismo SCOPE.'
        self.errrorText_MAIN_NOT_EXHISTS = 'No existe la definicion de un método MAIN sin PARAMETROS'
        self.errrorText_CANTIDAD_PARAMETROS = 'El número dado de argumentos en la llamada al método es la correcta'
        self.errrorText_TIPOMETODOS = 'No coincide el tipo de dato en los PARAMETROS del método dado. '
        self.errrorText_EQ_OPS = 'El tipo de dato de los operandos dados no es el mismo para sus valores. ( == != ) .'
        self.errrorText_ARITMETICA = 'El tipo de dato de operando debe ser INT para operaciones ARITMETICAS.'
        self.errrorText_REL_OP = 'El tipo de dato de un operando debe ser INT para REL_OPS.'
        self.errrorText_CONDICIONALES_GENERAL = 'En condiciones, el tipo de dato debe ser BOOLEAN'
        self.errrorText_IF = 'En un IF, el tipo de dato de ser BOOLEAN'
        self.errrorText_WHILE = 'En ciclos (WHILE) el valor DENTRO del while debe ser tipo BOOLEAN'
        self.errrorText_EQUALS = 'El valor de asignación no es del mismo tipo. Revise si tiene OTRO tipo de dato del declarado.'
        self.errrorText_TIPO_RETORNO = 'Un método debe retornar el mismo tipo de dato que DECLARO.'
        self.errrorText_TIPOVOID = 'Un método VOID no retorna NADA. Revise.'
        self.errrorText_ESTRUCTURAGENERAL = 'El tipo de dato debe ser STRUCT o ESTRUCTURA.'
        self.errrorText_METODO_NO_DECLARADO = 'No hay un método con este nombre. No existe o no esta definido en el SCOPE.'
        self.errrorText_VAR_REPETIDA = 'No es posible declarar una variable con el mismo nombre de un método. Tenga imaginación.'

    def AddEntryToTable(self, linea, columna, mensaje):
        """
        Método para agregar un nuevo error al stack
        *@param linea: la linea
        *@param columna:la columna
        *@param mensaje: el mensaje
        """
        self.errores.append({
            'Line': linea,
            'Col': columna,
            'Msg': mensaje
        })

    def getAllErrors(self):
        """
        Retorna todos los errores de error.
        """
        innerArray = []
        for error in self.errores:
            innerArray.append(
                'Linea: ' + str(error['Line']) + ':' + str(error['Col']) + ' ======> ' + error['Msg'])
        return innerArray
