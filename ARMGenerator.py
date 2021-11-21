class MIPS:

    def __init__(self, datosFunciones):
        self.datosFuncion = datosFunciones
        self.registrosArg = ['$a0', '$a1', '$a2', '$a3']
        print(self.datosFuncion)

    def construirGOTO(self, etiqueta):
        # hay varios tipos de jumps
        retorno = f"j {etiqueta}"
        pass

    def construirEtiqueta(self, etiqueta):
        print(f"{etiqueta}:")
        self.construirConfiguracionStack(etiqueta)

    def guardarParametrosEnStack(self, cantidadParametros):
        registrosParametros = ['$a0', '$a1', '$a2', '$a3']
        print("\t# Guardar en Stack los parametros de la funcion")
        for i in range(cantidadParametros):
            print(f"\tsw {registrosParametros.pop(0)}, {4 * i}($fp)")

    def construirConfiguracionStack(self, etiqueta):
        if (etiqueta == 'main'):
            ancho = self.datosFuncion[etiqueta].ancho
            if(ancho != 0):
                # Hay variables en main, preparar stack
                print(f'''
\t# Preparar stack
\tsw $fp, ($sp)
\tsub $fp, $sp, {ancho}
\tla $sp, ($fp)
                ''')
        elif (etiqueta != 'OutputInt'):
            # es cualquier funcion
            ancho = self.datosFuncion[etiqueta].ancho
            if(ancho != 0):
                # hay variables
                print(f'''
\t# Preparar stack
\tsub $sp, $sp, 4
\tsw, $ra, ($sp)
\tsub $sp, $sp, 4
\tsw $fp, ($sp)
\tsub $fp, $sp, {ancho}
\tla $sp, ($fp)
                ''')
                if(len(self.datosFuncion[etiqueta].argumentosTipos) > 0):
                    self.guardarParametrosEnStack(
                        len(self.datosFuncion[etiqueta].argumentosTipos))

    def construirIf(self, Rsrc, etiqueta):

        retorno = f"bgtz {Rsrc}, {etiqueta}"
        pass

    def construirMultiplicacion(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"mul {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirSuma(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"add {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirMenos(self, Rdest, Rsrc1):
        retorno = f"neg {Rdest}, {Rsrc1}"
        pass

    def construirResta(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"sub {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirNegacion(self, Rdest, Rsrc1):
        retorno = f"not {Rdest}, {Rsrc1}"
        pass

    def construirAnd(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"and {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirOr(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"or {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirComparacionIgual(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"seq {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirComparacionMayorIgual(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"sge {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirComparacionMayor(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"sgt {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirComparacionMenorIgual(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"sle {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirComparacionMenor(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"slt {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirComparacionNoIgual(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"sne {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirCarga(self, Rdest, Rsrc):
        retorno = f"move {Rdest}, {Rsrc}"
        pass

    def construirAlmacenamiento(self, Rsrc, direccion):

        retorno = f"sw {Rsrc}, {direccion}"
        pass

    '''
        Funciones
    '''

    def construirLlamarFuncion(self, nombre):
        print(f"\tjal {nombre}")

    def construirRetorno(self, reg):
        retorno = f"move $v0, {reg}"
        retorno += "jr $ra"
        self.restablecerRegistroParametros()

    def construirParametro(self, parametro):
        if (parametro.find('fp') != -1):
            offset = parametro[parametro.find('[') + 1:parametro.find(']')]
            print(f"""\t# Cargar parametros
\tlw {self.registrosArg.pop(0)}, {offset}($fp)""")

    def construirRetornoSimple(self):
        '''
            Transfiere el control de nuevo a la llamada de funcion
        '''
        print('\tjr $ra')
        self.restablecerRegistroParametros()

    def constuirInputInt(self):
        print('''
\t# Se imprime mensaje al usuario
\tli $v0, 4
\tla $a0, mensajeInput
\tsyscall

\t# Se lee el input del usuario
\tli $v0,5
\tsyscall
\tjr $ra
        ''')

    def constuirOutputInt(self):
        print('''
\t# Se imprime numero en pantalla
\tli $v0, 1
\tsyscall

\t# Se hace un salto de linea
\tli $v0, 4
\tla $a0, saltoLinea
\tsyscall
\tjr $ra
        ''')

    '''
        Complementarias
    '''

    def restablecerRegistroParametros(self):
        self.registrosArg = ['$a0', '$a1', '$a2', '$a3']

    def encabezado(self, espacioGlobal):
        newLine = "\n"
        print(f'''
.data
.align 2
    G_: .space {espacioGlobal}
    mensajeInput: .asciiz "Ingrese un número entero: "
    saltoLinea: .asciiz "{repr(newLine).replace("'","")}"
.text
        ''')

    def encabezadoV2(self, espacioGlobal):
        print(f'''
.section .text
.global _start
_start:

        ''')

    def finPrograma(self):
        print('''
\t# fin del programa
\tli $v0, 10
\tsyscall
        ''')

    def generarCodigo(self, cuadruplas):
        funcionActual = ""
        for linea in cuadruplas:
            if linea.op == 'FUNCTION':
                self.construirEtiqueta(linea.arg1)
                funcionActual = linea.arg1
                if(linea.arg1 == 'InputInt'):
                    self.constuirInputInt()
                elif(linea.arg1 == 'OutputInt'):
                    self.constuirOutputInt()
            elif linea.op == 'RETURN':
                if (funcionActual == 'InputInt'):
                    self.construirRetornoSimple()

            elif linea.op == 'END FUNCTION':
                funcionActual = ""
            elif linea.op == 'CALL':
                self.construirLlamarFuncion(linea.arg1)
            elif linea.op == 'PARAM':
                self.construirParametro(linea.arg1)

            else:
                linea.debug()

    def __repr__(self):
        return f""
