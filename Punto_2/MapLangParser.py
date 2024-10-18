# Generated from MapLang.g4 by ANTLR 4.13.2
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
        4,1,9,59,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,3,3,29,8,
        3,1,4,1,4,1,4,1,4,5,4,35,8,4,10,4,12,4,38,9,4,3,4,40,8,4,1,4,1,4,
        1,5,1,5,1,5,1,5,5,5,48,8,5,10,5,12,5,51,9,5,3,5,53,8,5,1,5,1,5,1,
        6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,7,8,56,0,14,1,0,0,0,2,17,
        1,0,0,0,4,24,1,0,0,0,6,28,1,0,0,0,8,30,1,0,0,0,10,43,1,0,0,0,12,
        56,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,5,1,0,
        0,18,19,5,2,0,0,19,20,3,4,2,0,20,21,5,3,0,0,21,22,3,6,3,0,22,23,
        5,4,0,0,23,3,1,0,0,0,24,25,5,7,0,0,25,5,1,0,0,0,26,29,3,8,4,0,27,
        29,3,10,5,0,28,26,1,0,0,0,28,27,1,0,0,0,29,7,1,0,0,0,30,39,5,5,0,
        0,31,36,3,12,6,0,32,33,5,3,0,0,33,35,3,12,6,0,34,32,1,0,0,0,35,38,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,
        39,31,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,6,0,0,42,9,1,0,
        0,0,43,52,5,2,0,0,44,49,3,12,6,0,45,46,5,3,0,0,46,48,3,12,6,0,47,
        45,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,53,1,0,0,
        0,51,49,1,0,0,0,52,44,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,
        5,4,0,0,55,11,1,0,0,0,56,57,7,0,0,0,57,13,1,0,0,0,5,28,36,39,49,
        52
    ]

class MapLangParser ( Parser ):

    grammarFileName = "MapLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "NUMBER", "WS" ]

    RULE_program = 0
    RULE_mapExpression = 1
    RULE_function = 2
    RULE_iterable = 3
    RULE_list = 4
    RULE_tuple = 5
    RULE_expression = 6

    ruleNames =  [ "program", "mapExpression", "function", "iterable", "list", 
                   "tuple", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    IDENTIFIER=7
    NUMBER=8
    WS=9

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

        def mapExpression(self):
            return self.getTypedRuleContext(MapLangParser.MapExpressionContext,0)


        def EOF(self):
            return self.getToken(MapLangParser.EOF, 0)

        def getRuleIndex(self):
            return MapLangParser.RULE_program

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

        localctx = MapLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.mapExpression()
            self.state = 15
            self.match(MapLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(MapLangParser.FunctionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapLangParser.IterableContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_mapExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapExpression" ):
                listener.enterMapExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapExpression" ):
                listener.exitMapExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapExpression" ):
                return visitor.visitMapExpression(self)
            else:
                return visitor.visitChildren(self)




    def mapExpression(self):

        localctx = MapLangParser.MapExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mapExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(MapLangParser.T__0)
            self.state = 18
            self.match(MapLangParser.T__1)
            self.state = 19
            self.function()
            self.state = 20
            self.match(MapLangParser.T__2)
            self.state = 21
            self.iterable()
            self.state = 22
            self.match(MapLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapLangParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MapLangParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MapLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MapLangParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(MapLangParser.TupleContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = MapLangParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_iterable)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.list_()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.tuple_()
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MapLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MapLangParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MapLangParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MapLangParser.T__4)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 31
                self.expression()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 32
                    self.match(MapLangParser.T__2)
                    self.state = 33
                    self.expression()
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 41
            self.match(MapLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MapLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MapLangParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = MapLangParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MapLangParser.T__1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 44
                self.expression()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 45
                    self.match(MapLangParser.T__2)
                    self.state = 46
                    self.expression()
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 54
            self.match(MapLangParser.T__3)
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

        def IDENTIFIER(self):
            return self.getToken(MapLangParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(MapLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return MapLangParser.RULE_expression

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

        localctx = MapLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





