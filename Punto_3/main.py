import sys
from antlr4 import *
from LaplaceTransformLexer import LaplaceTransformLexer
from LaplaceTransformParser import LaplaceTransformParser
from LaplaceVisitor import LaplaceVisitor

def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = LaplaceTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaplaceTransformParser(stream)
    tree = parser.program()
    visitor = LaplaceVisitor()
    result = visitor.visit(tree)
    print(f"Laplace Transform: {result}")

if __name__ == '__main__':
    main(sys.argv)
