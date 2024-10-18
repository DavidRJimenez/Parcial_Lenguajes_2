# Generated from Racional.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RacionalParser import RacionalParser
else:
    from RacionalParser import RacionalParser

# This class defines a complete listener for a parse tree produced by RacionalParser.
class RacionalListener(ParseTreeListener):

    # Enter a parse tree produced by RacionalParser#prog.
    def enterProg(self, ctx:RacionalParser.ProgContext):
        pass

    # Exit a parse tree produced by RacionalParser#prog.
    def exitProg(self, ctx:RacionalParser.ProgContext):
        pass


    # Enter a parse tree produced by RacionalParser#expr.
    def enterExpr(self, ctx:RacionalParser.ExprContext):
        pass

    # Exit a parse tree produced by RacionalParser#expr.
    def exitExpr(self, ctx:RacionalParser.ExprContext):
        pass


    # Enter a parse tree produced by RacionalParser#term.
    def enterTerm(self, ctx:RacionalParser.TermContext):
        pass

    # Exit a parse tree produced by RacionalParser#term.
    def exitTerm(self, ctx:RacionalParser.TermContext):
        pass


    # Enter a parse tree produced by RacionalParser#factor.
    def enterFactor(self, ctx:RacionalParser.FactorContext):
        pass

    # Exit a parse tree produced by RacionalParser#factor.
    def exitFactor(self, ctx:RacionalParser.FactorContext):
        pass



del RacionalParser