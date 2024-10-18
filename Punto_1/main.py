import sys
from antlr4 import *
from RacionalLexer import RacionalLexer
from RacionalParser import RacionalParser
from EvalVisitor import EvalVisitor

def main(argv):
    input_file = argv[1]
    with open(input_file, 'r') as file:
        lines = file.readlines()
    lexer = RacionalLexer(None)
    stream = CommonTokenStream(lexer)
    parser = RacionalParser(stream)
    evaluator = EvalVisitor()

    for line in lines:
        input_stream = InputStream(line.strip())
        lexer.inputStream = input_stream
        lexer.reset()
        stream.setTokenSource(lexer)
        parser.setInputStream(stream)
        tree = parser.prog()
        result = evaluator.visit(tree)
        print(f"Result of '{line.strip()}': {result} = {result.numerator}/{result.denominator}")

if __name__ == '__main__':
    main(sys.argv)
