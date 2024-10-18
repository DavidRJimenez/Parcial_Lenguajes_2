# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceTransformParser import LaplaceTransformParser
else:
    from LaplaceTransformParser import LaplaceTransformParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceTransformParser.

class LaplaceTransformVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceTransformParser#program.
    def visitProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#statement.
    def visitStatement(self, ctx:LaplaceTransformParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#laplaceExpression.
    def visitLaplaceExpression(self, ctx:LaplaceTransformParser.LaplaceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#expression.
    def visitExpression(self, ctx:LaplaceTransformParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#term.
    def visitTerm(self, ctx:LaplaceTransformParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#factor.
    def visitFactor(self, ctx:LaplaceTransformParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#base.
    def visitBase(self, ctx:LaplaceTransformParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#exponent.
    def visitExponent(self, ctx:LaplaceTransformParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#specificFunction.
    def visitSpecificFunction(self, ctx:LaplaceTransformParser.SpecificFunctionContext):
        return self.visitChildren(ctx)



del LaplaceTransformParser