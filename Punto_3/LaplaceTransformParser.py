# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,3,1,
        4,1,4,1,4,5,4,45,8,4,10,4,12,4,48,9,4,1,5,1,5,1,5,3,5,53,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,62,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,71,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,112,8,8,1,8,0,0,9,0,2,4,
        6,8,10,12,14,16,0,2,1,0,19,20,1,0,21,22,128,0,21,1,0,0,0,2,26,1,
        0,0,0,4,28,1,0,0,0,6,33,1,0,0,0,8,41,1,0,0,0,10,49,1,0,0,0,12,61,
        1,0,0,0,14,70,1,0,0,0,16,111,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,
        20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,
        0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,3,4,2,0,27,3,1,0,0,0,28,29,
        5,1,0,0,29,30,5,2,0,0,30,31,3,6,3,0,31,32,5,3,0,0,32,5,1,0,0,0,33,
        38,3,8,4,0,34,35,7,0,0,0,35,37,3,8,4,0,36,34,1,0,0,0,37,40,1,0,0,
        0,38,36,1,0,0,0,38,39,1,0,0,0,39,7,1,0,0,0,40,38,1,0,0,0,41,46,3,
        10,5,0,42,43,7,1,0,0,43,45,3,10,5,0,44,42,1,0,0,0,45,48,1,0,0,0,
        46,44,1,0,0,0,46,47,1,0,0,0,47,9,1,0,0,0,48,46,1,0,0,0,49,52,3,12,
        6,0,50,51,5,23,0,0,51,53,3,14,7,0,52,50,1,0,0,0,52,53,1,0,0,0,53,
        11,1,0,0,0,54,62,3,16,8,0,55,62,5,25,0,0,56,62,5,24,0,0,57,58,5,
        2,0,0,58,59,3,6,3,0,59,60,5,3,0,0,60,62,1,0,0,0,61,54,1,0,0,0,61,
        55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,62,13,1,0,0,0,63,71,3,16,
        8,0,64,71,5,25,0,0,65,71,5,24,0,0,66,67,5,2,0,0,67,68,3,6,3,0,68,
        69,5,3,0,0,69,71,1,0,0,0,70,63,1,0,0,0,70,64,1,0,0,0,70,65,1,0,0,
        0,70,66,1,0,0,0,71,15,1,0,0,0,72,73,5,4,0,0,73,74,5,2,0,0,74,75,
        3,6,3,0,75,76,5,3,0,0,76,112,1,0,0,0,77,78,5,5,0,0,78,79,5,2,0,0,
        79,80,3,6,3,0,80,81,5,3,0,0,81,112,1,0,0,0,82,83,5,6,0,0,83,84,5,
        2,0,0,84,85,3,6,3,0,85,86,5,3,0,0,86,112,1,0,0,0,87,88,5,7,0,0,88,
        89,5,2,0,0,89,90,3,6,3,0,90,91,5,3,0,0,91,112,1,0,0,0,92,93,5,8,
        0,0,93,94,5,2,0,0,94,95,3,6,3,0,95,96,5,3,0,0,96,112,1,0,0,0,97,
        98,5,9,0,0,98,99,5,2,0,0,99,100,3,6,3,0,100,101,5,3,0,0,101,112,
        1,0,0,0,102,112,5,10,0,0,103,112,5,11,0,0,104,112,5,12,0,0,105,112,
        5,13,0,0,106,112,5,14,0,0,107,112,5,15,0,0,108,112,5,16,0,0,109,
        112,5,17,0,0,110,112,5,18,0,0,111,72,1,0,0,0,111,77,1,0,0,0,111,
        82,1,0,0,0,111,87,1,0,0,0,111,92,1,0,0,0,111,97,1,0,0,0,111,102,
        1,0,0,0,111,103,1,0,0,0,111,104,1,0,0,0,111,105,1,0,0,0,111,106,
        1,0,0,0,111,107,1,0,0,0,111,108,1,0,0,0,111,109,1,0,0,0,111,110,
        1,0,0,0,112,17,1,0,0,0,7,21,38,46,52,61,70,111
    ]

class LaplaceTransformParser ( Parser ):

    grammarFileName = "LaplaceTransform.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Laplace'", "'('", "')'", "'exp'", "'sin'", 
                     "'cos'", "'sinh'", "'cosh'", "'unit_step'", "'delta_t_tau'", 
                     "'delta_t'", "'t_n_exp'", "'unit_step_tau'", "'t_n'", 
                     "'t_q'", "'log'", "'bessel_first'", "'bessel_mod'", 
                     "'+'", "'-'", "'*'", "'/'", "'**'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MINUS", 
                      "MUL", "DIV", "POW", "IDENTIFIER", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_laplaceExpression = 2
    RULE_expression = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_base = 6
    RULE_exponent = 7
    RULE_specificFunction = 8

    ruleNames =  [ "program", "statement", "laplaceExpression", "expression", 
                   "term", "factor", "base", "exponent", "specificFunction" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    PLUS=19
    MINUS=20
    MUL=21
    DIV=22
    POW=23
    IDENTIFIER=24
    NUMBER=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LaplaceTransformParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.StatementContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.StatementContext,i)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LaplaceTransformParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(LaplaceTransformParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def laplaceExpression(self):
            return self.getTypedRuleContext(LaplaceTransformParser.LaplaceExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LaplaceTransformParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.laplaceExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LaplaceExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_laplaceExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaplaceExpression" ):
                listener.enterLaplaceExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaplaceExpression" ):
                listener.exitLaplaceExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLaplaceExpression" ):
                return visitor.visitLaplaceExpression(self)
            else:
                return visitor.visitChildren(self)




    def laplaceExpression(self):

        localctx = LaplaceTransformParser.LaplaceExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_laplaceExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(LaplaceTransformParser.T__0)
            self.state = 29
            self.match(LaplaceTransformParser.T__1)
            self.state = 30
            self.expression()
            self.state = 31
            self.match(LaplaceTransformParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.TermContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceTransformParser.PLUS)
            else:
                return self.getToken(LaplaceTransformParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceTransformParser.MINUS)
            else:
                return self.getToken(LaplaceTransformParser.MINUS, i)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = LaplaceTransformParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.term()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self.term()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.FactorContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceTransformParser.MUL)
            else:
                return self.getToken(LaplaceTransformParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceTransformParser.DIV)
            else:
                return self.getToken(LaplaceTransformParser.DIV, i)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LaplaceTransformParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.factor()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 42
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43
                self.factor()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base(self):
            return self.getTypedRuleContext(LaplaceTransformParser.BaseContext,0)


        def POW(self):
            return self.getToken(LaplaceTransformParser.POW, 0)

        def exponent(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExponentContext,0)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = LaplaceTransformParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.base()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 50
                self.match(LaplaceTransformParser.POW)
                self.state = 51
                self.exponent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specificFunction(self):
            return self.getTypedRuleContext(LaplaceTransformParser.SpecificFunctionContext,0)


        def NUMBER(self):
            return self.getToken(LaplaceTransformParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(LaplaceTransformParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase" ):
                listener.enterBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase" ):
                listener.exitBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase" ):
                return visitor.visitBase(self)
            else:
                return visitor.visitChildren(self)




    def base(self):

        localctx = LaplaceTransformParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.specificFunction()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(LaplaceTransformParser.NUMBER)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(LaplaceTransformParser.IDENTIFIER)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(LaplaceTransformParser.T__1)
                self.state = 58
                self.expression()
                self.state = 59
                self.match(LaplaceTransformParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specificFunction(self):
            return self.getTypedRuleContext(LaplaceTransformParser.SpecificFunctionContext,0)


        def NUMBER(self):
            return self.getToken(LaplaceTransformParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(LaplaceTransformParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)




    def exponent(self):

        localctx = LaplaceTransformParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exponent)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.specificFunction()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(LaplaceTransformParser.NUMBER)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(LaplaceTransformParser.IDENTIFIER)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(LaplaceTransformParser.T__1)
                self.state = 67
                self.expression()
                self.state = 68
                self.match(LaplaceTransformParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_specificFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecificFunction" ):
                listener.enterSpecificFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecificFunction" ):
                listener.exitSpecificFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecificFunction" ):
                return visitor.visitSpecificFunction(self)
            else:
                return visitor.visitChildren(self)




    def specificFunction(self):

        localctx = LaplaceTransformParser.SpecificFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_specificFunction)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(LaplaceTransformParser.T__3)
                self.state = 73
                self.match(LaplaceTransformParser.T__1)
                self.state = 74
                self.expression()
                self.state = 75
                self.match(LaplaceTransformParser.T__2)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(LaplaceTransformParser.T__4)
                self.state = 78
                self.match(LaplaceTransformParser.T__1)
                self.state = 79
                self.expression()
                self.state = 80
                self.match(LaplaceTransformParser.T__2)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.match(LaplaceTransformParser.T__5)
                self.state = 83
                self.match(LaplaceTransformParser.T__1)
                self.state = 84
                self.expression()
                self.state = 85
                self.match(LaplaceTransformParser.T__2)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.match(LaplaceTransformParser.T__6)
                self.state = 88
                self.match(LaplaceTransformParser.T__1)
                self.state = 89
                self.expression()
                self.state = 90
                self.match(LaplaceTransformParser.T__2)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.match(LaplaceTransformParser.T__7)
                self.state = 93
                self.match(LaplaceTransformParser.T__1)
                self.state = 94
                self.expression()
                self.state = 95
                self.match(LaplaceTransformParser.T__2)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.match(LaplaceTransformParser.T__8)
                self.state = 98
                self.match(LaplaceTransformParser.T__1)
                self.state = 99
                self.expression()
                self.state = 100
                self.match(LaplaceTransformParser.T__2)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 102
                self.match(LaplaceTransformParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 103
                self.match(LaplaceTransformParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 9)
                self.state = 104
                self.match(LaplaceTransformParser.T__11)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 10)
                self.state = 105
                self.match(LaplaceTransformParser.T__12)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 11)
                self.state = 106
                self.match(LaplaceTransformParser.T__13)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 12)
                self.state = 107
                self.match(LaplaceTransformParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 13)
                self.state = 108
                self.match(LaplaceTransformParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 14)
                self.state = 109
                self.match(LaplaceTransformParser.T__16)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 15)
                self.state = 110
                self.match(LaplaceTransformParser.T__17)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





