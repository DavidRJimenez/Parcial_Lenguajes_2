Instrucciones para Ejecutar los Programas

Este README proporciona instrucciones sobre cómo ejecutar los tres programas desarrollados en ANTLR y Python.
Requisitos Previos

    ANTLR: Asegúrate de tener ANTLR instalado. Puedes seguir las instrucciones en ANTLR para la instalación.

    Python: Asegúrate de tener Python instalado.

    SymPy: Para el tercer programa, asegúrate de tener la librería SymPy instalada. Puedes instalarla usando pip:
    sh

    pip install sympy


Yo use un entorno virtual en mi pc, pero lo explico por si el profe Joaquin necesita saberlo antes de.


Punto 1: Operaciones con Números Racionales
Gramática: Racional.g4

Esta gramática permite realizar operaciones con números racionales, como sumas y restas.
Comandos para Ejecutar

    Generar Archivos con ANTLR:
    sh

antlr4 -Dlanguage=Python3 -visitor Racional.g4

Ejecutar el Programa:
sh

    python3 main.py input.txt

Archivo de Prueba input.txt

Ejemplo de contenido:
txt

(1/3 + 2/3)

Punto 2: Aplicar Funciones sobre Ítems de Objetos Iterables
Gramática: MapLang.g4

Esta gramática permite aplicar funciones a los elementos de una lista o tupla y filtrar elementos según una condición.
Comandos para Ejecutar

    Generar Archivos con ANTLR:
    sh

antlr4 -Dlanguage=Python3 -visitor MapLang.g4

Ejecutar el Programa:
sh

    python3 main.py test.map

Archivo de Prueba input.txt

Ejemplo de contenido:
txt
MAP(funcion, [1, 2, 3])


Punto 3: Transformada de Laplace
Gramática: LaplaceTransform.g4

Esta gramática permite calcular la transformada de Laplace de una expresión matemática.
Comandos para Ejecutar

    Generar Archivos con ANTLR:
    sh

antlr4 -Dlanguage=Python3 -visitor LaplaceTransform.g4

Ejecutar el Programa:
sh

    python3 main.py input.txt

Archivo de Prueba input.txt

Ejemplo de contenido:
txt

Laplace(3*t**2 + 2*t + 1)


y listop.