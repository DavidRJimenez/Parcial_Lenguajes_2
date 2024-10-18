from MapLangParser import MapLangParser
from MapLangVisitor import MapLangVisitor

class CodeGenerator(MapLangVisitor):
    def visitProgram(self, ctx: MapLangParser.ProgramContext):
        return self.visit(ctx.mapExpression())

    def visitMapExpression(self, ctx: MapLangParser.MapExpressionContext):
        function = ctx.function().getText()
        iterable = self.visit(ctx.iterable())
        print(f"Visiting MapExpression: function={function}, iterable={iterable}")  # Para depuración
        return f'list(map({function}, {iterable}))'

    def visitList(self, ctx: MapLangParser.ListContext):
        elements = [self.visit(expr) for expr in ctx.expression()] if ctx.expression() else []
        print(f"Visiting List: elements={elements}")  # Para depuración
        return f'[{", ".join(elements)}]'

    def visitTuple(self, ctx: MapLangParser.TupleContext):
        elements = [self.visit(expr) for expr in ctx.expression()] if ctx.expression() else []
        print(f"Visiting Tuple: elements={elements}")  # Para depuración
        return f'({", ".join(elements)})'

    def visitExpression(self, ctx: MapLangParser.ExpressionContext):
        print(f"Visiting Expression: {ctx.getText()}")  # Para depuración
        return ctx.getText()
