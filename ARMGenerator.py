class ARGCodigoGenerador:

    def __init__(self):
        self.valoresIniciales= ""

    def construirGOTO(self, etiqueta):
        # hay varios tipos de jumps
        retorno = f"j {etiqueta}"
        pass

    def construirMultiplicacion(self, registros):
        return f"\tmul {registros[0]}, {registros[1]}, {registros[2]}\n"

    def construirSuma(self, registros):
        return f"\tadd {registros[0]}, {registros[1]}, {registros[2]}\n"

    def construirSumaV2(self, registros, constante):
        return f"\tadd {registros[0]}, {registros[1]}, {constante}\n"


    def construirResta(self, registros):
        return f"\tsub {registros[0]}, {registros[1]}, {registros[2]}\n"


    def construirAnd(self, Rdest, Rsrc1, Rsrc2):
        retorno = f"and {Rdest}, {Rsrc1}, {Rsrc2}"
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
