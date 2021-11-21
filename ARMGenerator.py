class ARGCodigoGenerador:

    def __init__(self):
        self.base = ""

    def construirGOTO(self, etiqueta):
        # hay varios tipos de jumps
        retorno = f"j {etiqueta}"
        pass

    def construirIf(self, Rsrc, etiqueta):

        retorno = f"bgtz {Rsrc}, {etiqueta}"
        pass

    def construirMultiplicacion(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"mul {Rdest}, {Rsrc1}, {Rsrc2}"
        pass

    def construirSuma(self, cuadrupla):
        x = cuadrupla.resultado
        y = cuadrupla.arg1
        z = cuadrupla.arg2
        print("\t# Suma")

        self.descriptor.agregarAcceso(x)
        self.descriptor.agregarAcceso(y)
        self.descriptor.agregarAcceso(z)

        esLiteral = False
        literal = None
        try:
            y = int(y)
            esLiteral = True
            literal = y
        except:
            pass

        try:
            z = int(z)
            esLiteral = True
            literal = z
        except:
            pass

        registros = self.descriptor.getReg(x, y, z)
        if(esLiteral):
            print(
                f"\taddi {registros[0]}, {registros[1]}, {literal}")

        self.descriptor.eliminarAccesoTemporal(y)
        self.descriptor.eliminarAccesoTemporal(z)
        # print(self.descriptor.registro)
        # print(self.descriptor.acceso)
        # retorno = f"add {Rdest}, {Rsrc1}, {Rsrc2}"

    def construirDivision(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"div {Rdest}, {Rsrc1}, {Rsrc2}"
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


    def construirEncabezado(self):
        return(f'''
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

