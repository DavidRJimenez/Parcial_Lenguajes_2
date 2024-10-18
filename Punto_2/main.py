import sys
from antlr4 import *
from MapLangLexer import MapLangLexer
from MapLangParser import MapLangParser
from Codegenerator import CodeGenerator  # Asegúrate de que esta línea esté presente

def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = MapLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapLangParser(stream)
    tree = parser.program()  # Asegúrate de que 'program' sea la regla inicial de tu gramática
    generator = CodeGenerator()
    result = generator.visit(tree)  # Esto debería generar el código
    print(f"Generated code: {result}")  # Asegúrate de imprimir el resultado aquí

if __name__ == '__main__':
    main(sys.argv)
