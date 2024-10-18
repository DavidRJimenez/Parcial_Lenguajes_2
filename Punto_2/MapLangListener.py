# Generated from MapLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapLangParser import MapLangParser
else:
    from MapLangParser import MapLangParser

# This class defines a complete listener for a parse tree produced by MapLangParser.
class MapLangListener(ParseTreeListener):

    # Enter a parse tree produced by MapLangParser#program.
    def enterProgram(self, ctx:MapLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MapLangParser#program.
    def exitProgram(self, ctx:MapLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MapLangParser#mapExpression.
    def enterMapExpression(self, ctx:MapLangParser.MapExpressionContext):
        pass

    # Exit a parse tree produced by MapLangParser#mapExpression.
    def exitMapExpression(self, ctx:MapLangParser.MapExpressionContext):
        pass


    # Enter a parse tree produced by MapLangParser#function.
    def enterFunction(self, ctx:MapLangParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapLangParser#function.
    def exitFunction(self, ctx:MapLangParser.FunctionContext):
        pass


    # Enter a parse tree produced by MapLangParser#iterable.
    def enterIterable(self, ctx:MapLangParser.IterableContext):
        pass

    # Exit a parse tree produced by MapLangParser#iterable.
    def exitIterable(self, ctx:MapLangParser.IterableContext):
        pass


    # Enter a parse tree produced by MapLangParser#list.
    def enterList(self, ctx:MapLangParser.ListContext):
        pass

    # Exit a parse tree produced by MapLangParser#list.
    def exitList(self, ctx:MapLangParser.ListContext):
        pass


    # Enter a parse tree produced by MapLangParser#tuple.
    def enterTuple(self, ctx:MapLangParser.TupleContext):
        pass

    # Exit a parse tree produced by MapLangParser#tuple.
    def exitTuple(self, ctx:MapLangParser.TupleContext):
        pass


    # Enter a parse tree produced by MapLangParser#expression.
    def enterExpression(self, ctx:MapLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MapLangParser#expression.
    def exitExpression(self, ctx:MapLangParser.ExpressionContext):
        pass



del MapLangParser