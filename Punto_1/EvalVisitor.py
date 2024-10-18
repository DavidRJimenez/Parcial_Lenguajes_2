from fractions import Fraction
from RacionalParser import RacionalParser
from RacionalVisitor import RacionalVisitor

class EvalVisitor(RacionalVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
        else:
            return self.visit(ctx.getChild(0))

    def visitTerm(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op == '*':
                return left * right
            elif op == '/':
                return left / right
        else:
            return self.visit(ctx.getChild(0))

    def visitFactor(self, ctx):
        if ctx.RACIONAL():
            return self.to_rational(ctx.RACIONAL().getText())
        else:
            return self.visit(ctx.getChild(1))

    def to_rational(self, text):
        numerator, denominator = map(int, text.split('/'))
        return Fraction(numerator, denominator)
