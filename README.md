<h1 align="center">
<br>
  <img src="https://images-na.ssl-images-amazon.com/images/I/51FWXX9KWVL._AC_UL600_SR600,600_.jpg" alt="UkronTadd" width="664">
<br>
<br>
Proyecto 2: Generación de código intermedio
</h1>

<p align="center">

  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/static/v1?label=License&message=NoLicense&color=<COLOR>" alt="No license">
  </a>
</p>

<p align="center">University Project :mortar_board:</p>
<p align="center">Alejandro Tejada 17584</p>
<p align="center">Construccion de compiladores</p>
<p align="center">Universidad del Valle de Guatemala</p>
<p align="center">16/09/2021</p>
<hr />

# Acerca de...

Este proyecto es el segundo de tres de construccion de un compilador. Esta fase es la generación de código intermedio. El código intermedio es una fase intermedia entre el analisis semántico y el codigo a nivel de assembler, de esta forma, logramos hacer esta transición mas suave al tener algo más sencillo de traducir a lenguaje de máquina.
Algunos puntos vistos en este proyecto
- Traducción a código intermedio de expresiones
- Traducción a código intermedio de IF y While
- Traducción a código intermedio de Arrays, llamadas a métodos, parámetros, y operaciones.

# Descripción de herramientas  y archivos archivos

## Listado de herramientas usadas para el proyecto

- Python 3.8.0 64bits
- Compiladores principios, técnicas y herramientas, 2da Edición - Alfred V. Aho
- VS Code
- Windows Terminal
- A lot of Coffe (more Coffe than last time, A LOT) (**enought coffe for a life V4, version Intermediate Code**)


## Liberías NECESARIAS para correr el programa

- Python 3.8.0
  - Una versión de Python de la versión Python 3.6.0 64bits o mayor
- Pprint
  - Una librería de python para imprimir bonito. Si no se tiene instalar en https://pypi.org/project/pprintpp/
- Terminal
  - Una terminal o programa para correr los programas de python. Puede ser VS Code también.


## Archivos y carpetas
| No. | Archivo                          | Propósito/Descripción                                                                                                              |
| --- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `Python3`                        | Folder donde esta la gramática, los lexer, parser, etc. Acá dentro también se encuentran los archivos de prueba y lo que se prueba |
| 2   | `decafAlejandro.tokens`          | Tokens generados por ANTLR                                                                                                         |
| 3   | `decafAlejandroLexer.py`         | Es un python generado por ANTLR que contiene el lexer del proyecto                                                                 |
| 4   | `decafAlejandroListener.py`      | Contiene un listener, es decir, una forma de recorrer el arbol sintáctico generado                                                 |
| 5   | `decafAlejandroParser.py`        | el parser generador por ANTLR para el proyecto                                                                                     |
| 6   | `ErrorClass.py`                  | Una clase de errores para arrays o errores generales                                                                               |
| 7   | `funciones.py`                   | Un python con funciones generales y útiles                                                                                         |
| 8   |  `mainSemantic.py`                | programa más importante. Acá se genera la logica, los valores, y se revisan TODAS las reglas semánticas                            |
| 9   | `Gramática V2`         | Tenemos una nueva coleccion de una segunda gramática, esta se usó para eta fase, por ende veremos los mismos listener, tokens, y lexer soloq ue en V2                                                                                                        |
| 10  | `symbolTable.py`                 | Clase que contiene TODAS las declaraciones para las tres tablas de simbolos principales: metodos, variables y estructuras          |
| 11  | `NodoBoolean.py`                 | Un nodo para guardar las expresiones de algo complejo como un nodo IF       |
| 12  | `NodoCodigo.py`                 | Una clase nodo para guardar expresiones y address de las cosas       |
| 13 | `GUI.py`                 | La interfaz gráfica      |
| 14  | `Readme.md`                      | El readme                                                                                                                          |
| 15  | `Python3/Programas/multiple_tests.decaf` | El programa donde probamos por defecto                                                                                             |


<br>
<br>



## Cómo correr el proyecto

- Primero se debe editar en el file de `Python3/Programas/simple.decaf` con lo que deseemos poner a prueba. Por ejemplo:
  ```python
        class Program
        {

        int A[10];


        int Minimo(int i)
        {
          int Min;
          int index;
          Min = A[i];
          index = i;
          while(i<10)
          {
            if (A[i]<Min)
            {
              Min = A[i];
              index = i;
            }
            i = i + 1;
          }
          return index;
        }

        void Ordenar(void)
        {
          int i;
          int j;
          int temp;
          i = 0;
          while(i<10)
          {
            int Index;
            Index = Minimo(i);
            temp = A[Index];
            A[Index] = A[i];
            A[i]=temp;
            i = i+1;
          }
        }



        void OutputInt(int n)
        {
        }

        int InputInt(void)
        {return 0;}


        void main(void)
        {

          int i;
          i = 0;
          while(i<10)
          {
            A[i]=InputInt();
            i = i+1;		
          }
          Ordenar();
          i = 0;
          while(i<10)
          {
            OutputInt(A[i]);
            i = i+1;
          }

        }


        }
  ```
- Luego, se debe correr el  programa `GUI.py` y ejecutarlo en una consola. 
- Luego se debe de buscar el file con ABRIR file, luego, editar en el espacio lo que necesitemos.
- Finalmente, presionar COMPILAR INTERMEDIO. Y el código intermedio aparecerá en la parte del texto donde debería.

## Creditos y Agradecimientos

Course teacher: Bidkar Pojoy

- https://graphviz.org/about/
- https://graphviz.org/documentation/
- https://www.tutorialspoint.com/c_standard_library/time_h.htm
- https://docs.python.org/3/library/time.html
- Compiladores principios, técnicas y herramientas, 2da Edición - Alfred V. Aho
- Compañeros de clase
- More Coffe
- Coffe machine right next to me


## Licence

Bajo la propia del desarrollador.