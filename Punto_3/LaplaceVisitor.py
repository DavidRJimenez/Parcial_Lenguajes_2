from LaplaceTransformParser import LaplaceTransformParser
from LaplaceTransformVisitor import LaplaceTransformVisitor
import sympy as sp

class LaplaceVisitor(LaplaceTransformVisitor):
    def visitProgram(self, ctx: LaplaceTransformParser.ProgramContext):
        return self.visit(ctx.statement(0))

    def visitLaplaceExpression(self, ctx: LaplaceTransformParser.LaplaceExpressionContext):
        expr = self.visit(ctx.expression())
        t, s = sp.symbols('t s')
        laplace_expr = sp.laplace_transform(expr, t, s)
        return laplace_expr[0]

    def visitExpression(self, ctx: LaplaceTransformParser.ExpressionContext):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            if ctx.getChild(2 * i - 1).getText() == '+':
                result += self.visit(ctx.term(i))
            elif ctx.getChild(2 * i - 1).getText() == '-':
                result -= self.visit(ctx.term(i))
        return result

    def visitTerm(self, ctx: LaplaceTransformParser.TermContext):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operator = ctx.getChild(2 * i - 1).getText()
            if operator == '*':
                result *= self.visit(ctx.factor(i))
            elif operator == '/':
                result /= self.visit(ctx.factor(i))
        return result

    def visitFactor(self, ctx: LaplaceTransformParser.FactorContext):
        base = self.visit(ctx.base())
        if ctx.POW():
            exponent = self.visit(ctx.exponent())
            return base**exponent
        return base

    def visitBase(self, ctx: LaplaceTransformParser.BaseContext):
        if ctx.NUMBER():
            return sp.sympify(ctx.NUMBER().getText())
        elif ctx.IDENTIFIER():
            return sp.symbols(ctx.IDENTIFIER().getText())
        elif ctx.specificFunction():
            return self.visit(ctx.specificFunction())
        elif ctx.expression():
            return self.visit(ctx.expression())

    def visitExponent(self, ctx: LaplaceTransformParser.ExponentContext):
        return self.visitBase(ctx)

    def visitSpecificFunction(self, ctx: LaplaceTransformParser.SpecificFunctionContext):
        func_name = ctx.getText()
        t = sp.symbols('t')
        if func_name.startswith('exp'):
            inner_expr = self.visit(ctx.expression())
            return sp.exp(inner_expr)
        elif func_name.startswith('sin'):
            inner_expr = self.visit(ctx.expression())
            return sp.sin(inner_expr)
        elif func_name.startswith('cos'):
            inner_expr = self.visit(ctx.expression())
            return sp.cos(inner_expr)
        elif func_name.startswith('sinh'):
            inner_expr = self.visit(ctx.expression())
            return sp.sinh(inner_expr)
        elif func_name.startswith('cosh'):
            inner_expr = self.visit(ctx.expression())
            return sp.cosh(inner_expr)
        elif func_name.startswith('unit_step'):
            inner_expr = self.visit(ctx.expression())
            return sp.Heaviside(inner_expr)
        elif func_name == 'delta_t_tau':
            return sp.DiracDelta(t - sp.Symbol('tau'))
        elif func_name == 'delta_t':
            return sp.DiracDelta(t)
        elif func_name == 't_n_exp':
            return t**sp.Symbol('n') * sp.exp(t)
        elif func_name == 'unit_step_tau':
            return sp.Heaviside(t - sp.Symbol('tau'))
        elif func_name == 't_n':
            return t**sp.Symbol('n')
        elif func_name == 't_q':
            return t**sp.Symbol('q')
        elif func_name == 'log':
            return sp.log(t)
        elif func_name == 'bessel_first':
            return sp.besselj(0, t)
        elif func_name == 'bessel_mod':
            return sp.besseli(0, t)
