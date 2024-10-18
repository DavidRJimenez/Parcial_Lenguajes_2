# Generated from Racional.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RacionalParser import RacionalParser
else:
    from RacionalParser import RacionalParser

# This class defines a complete generic visitor for a parse tree produced by RacionalParser.

class RacionalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RacionalParser#prog.
    def visitProg(self, ctx:RacionalParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalParser#expr.
    def visitExpr(self, ctx:RacionalParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalParser#term.
    def visitTerm(self, ctx:RacionalParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalParser#factor.
    def visitFactor(self, ctx:RacionalParser.FactorContext):
        return self.visitChildren(ctx)



del RacionalParser