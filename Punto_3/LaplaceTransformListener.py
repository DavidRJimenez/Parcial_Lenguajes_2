# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceTransformParser import LaplaceTransformParser
else:
    from LaplaceTransformParser import LaplaceTransformParser

# This class defines a complete listener for a parse tree produced by LaplaceTransformParser.
class LaplaceTransformListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceTransformParser#program.
    def enterProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#program.
    def exitProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#statement.
    def enterStatement(self, ctx:LaplaceTransformParser.StatementContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#statement.
    def exitStatement(self, ctx:LaplaceTransformParser.StatementContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#laplaceExpression.
    def enterLaplaceExpression(self, ctx:LaplaceTransformParser.LaplaceExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#laplaceExpression.
    def exitLaplaceExpression(self, ctx:LaplaceTransformParser.LaplaceExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#expression.
    def enterExpression(self, ctx:LaplaceTransformParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#expression.
    def exitExpression(self, ctx:LaplaceTransformParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#term.
    def enterTerm(self, ctx:LaplaceTransformParser.TermContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#term.
    def exitTerm(self, ctx:LaplaceTransformParser.TermContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#factor.
    def enterFactor(self, ctx:LaplaceTransformParser.FactorContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#factor.
    def exitFactor(self, ctx:LaplaceTransformParser.FactorContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#base.
    def enterBase(self, ctx:LaplaceTransformParser.BaseContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#base.
    def exitBase(self, ctx:LaplaceTransformParser.BaseContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#exponent.
    def enterExponent(self, ctx:LaplaceTransformParser.ExponentContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#exponent.
    def exitExponent(self, ctx:LaplaceTransformParser.ExponentContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#specificFunction.
    def enterSpecificFunction(self, ctx:LaplaceTransformParser.SpecificFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#specificFunction.
    def exitSpecificFunction(self, ctx:LaplaceTransformParser.SpecificFunctionContext):
        pass



del LaplaceTransformParser