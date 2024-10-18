# Generated from MapLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapLangParser import MapLangParser
else:
    from MapLangParser import MapLangParser

# This class defines a complete generic visitor for a parse tree produced by MapLangParser.

class MapLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapLangParser#program.
    def visitProgram(self, ctx:MapLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#mapExpression.
    def visitMapExpression(self, ctx:MapLangParser.MapExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#function.
    def visitFunction(self, ctx:MapLangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#iterable.
    def visitIterable(self, ctx:MapLangParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#list.
    def visitList(self, ctx:MapLangParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#tuple.
    def visitTuple(self, ctx:MapLangParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#expression.
    def visitExpression(self, ctx:MapLangParser.ExpressionContext):
        return self.visitChildren(ctx)



del MapLangParser