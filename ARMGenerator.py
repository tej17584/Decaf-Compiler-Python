class ARGCodigoGenerador:

    def __init__(self):
        self.base = ""

    def construirGOTO(self, etiqueta):
        # hay varios tipos de jumps
        retorno = f"j {etiqueta}"
        pass

    def construirIf(self, Rsrc, etiqueta):

        retorno = f"bgtz {Rsrc}, {etiqueta}"
        return retorno

    def construirMultiplicacion(self, registros):
        return f"\tmul {registros[0]}, {registros[1]}, {registros[2]}\n"

    def construirSuma(self, registros):
        return f"\tadd {registros[0]}, {registros[1]}, {registros[2]}\n"

    def cosntruirNegacion(self, Rdest, Rsrc1):
        retorno = f"neg {Rdest}, {Rsrc1}"
        pass

    def construirResta(self, registros):
        return f"\tsub {registros[0]}, {registros[1]}, {registros[2]}\n"

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

    def construirEncabezado(self, nombreHeader):
        return(f'''
.section .text
.global {nombreHeader}
{nombreHeader}:
''')

    def construirFuncionNueva(self, nombre):
        return(f'''

{nombre}:

''')

    def alocarEspacioMetodo(self, sizeTotal):
        retorno = f"\tsub sp, sp, #{sizeTotal}\n"
        return retorno

    def finPrograma(self):
        print('''
\t# fin del programa
\tli $v0, 10
\tsyscall
        ''')
