# Generated from Test.g4 by ANTLR 4.13.0
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
        4,1,41,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,4,0,17,8,0,11,0,12,0,18,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,3,4,36,8,4,1,5,1,5,1,6,1,6,1,6,0,0,
        7,0,2,4,6,8,10,12,0,1,1,0,34,36,36,0,14,1,0,0,0,2,23,1,0,0,0,4,25,
        1,0,0,0,6,31,1,0,0,0,8,35,1,0,0,0,10,37,1,0,0,0,12,39,1,0,0,0,14,
        16,5,24,0,0,15,17,3,2,1,0,16,15,1,0,0,0,17,18,1,0,0,0,18,16,1,0,
        0,0,18,19,1,0,0,0,19,20,1,0,0,0,20,21,5,25,0,0,21,22,5,0,0,1,22,
        1,1,0,0,0,23,24,3,4,2,0,24,3,1,0,0,0,25,26,3,10,5,0,26,27,3,6,3,
        0,27,28,5,17,0,0,28,29,3,12,6,0,29,30,5,22,0,0,30,5,1,0,0,0,31,32,
        5,37,0,0,32,7,1,0,0,0,33,36,3,10,5,0,34,36,5,23,0,0,35,33,1,0,0,
        0,35,34,1,0,0,0,36,9,1,0,0,0,37,38,7,0,0,0,38,11,1,0,0,0,39,40,5,
        38,0,0,40,13,1,0,0,0,2,18,35
    ]

class TestParser ( Parser ):

    grammarFileName = "Test.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'#'", "'add'", "'sub'", 
                     "'mul'", "'div'", "'mod'", "'eq'", "'ne'", "'gt'", 
                     "'lt'", "'ge'", "'le'", "'and'", "'or'", "'not'", "':='", 
                     "'{'", "'}'", "'('", "')'", "';'", "'void'", "'BEGIN'", 
                     "'END'", "'function'", "'print'", "'if'", "'returns'", 
                     "'stop'", "'next'", "'while'", "'then'", "'int'", "'boolean'", 
                     "'real'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENTS", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULE", "EQUALS", "NOT_EQUALS", "GREATER_THAN", 
                      "LESS_THAN", "GREATER_EQUAL", "LESS_EQUAL", "AND", 
                      "OR", "NOT", "ASSIGN", "OPEN_BLOCK", "CLOSE_BLOCK", 
                      "OPEN_ARGUMENTS", "CLOSE_ARGUMENTS", "END_OF_INSTRUCTION", 
                      "VOID", "BEGIN", "END", "DEF_FUNC", "ST_OUTPUT", "IF", 
                      "RETURN", "BREAK", "CONTINUE", "WHILE", "THEN", "INTEGER", 
                      "BOOLEAN", "DOUBLE", "ID", "NUMBER", "BOOLEAN_VALUES", 
                      "TRUE", "FALSE" ]

    RULE_main = 0
    RULE_instruction = 1
    RULE_assign = 2
    RULE_variableId = 3
    RULE_value_type = 4
    RULE_variable_type = 5
    RULE_digit = 6

    ruleNames =  [ "main", "instruction", "assign", "variableId", "value_type", 
                   "variable_type", "digit" ]

    EOF = Token.EOF
    WS=1
    COMMENTS=2
    PLUS=3
    MINUS=4
    MULTIPLY=5
    DIVIDE=6
    MODULE=7
    EQUALS=8
    NOT_EQUALS=9
    GREATER_THAN=10
    LESS_THAN=11
    GREATER_EQUAL=12
    LESS_EQUAL=13
    AND=14
    OR=15
    NOT=16
    ASSIGN=17
    OPEN_BLOCK=18
    CLOSE_BLOCK=19
    OPEN_ARGUMENTS=20
    CLOSE_ARGUMENTS=21
    END_OF_INSTRUCTION=22
    VOID=23
    BEGIN=24
    END=25
    DEF_FUNC=26
    ST_OUTPUT=27
    IF=28
    RETURN=29
    BREAK=30
    CONTINUE=31
    WHILE=32
    THEN=33
    INTEGER=34
    BOOLEAN=35
    DOUBLE=36
    ID=37
    NUMBER=38
    BOOLEAN_VALUES=39
    TRUE=40
    FALSE=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(TestParser.BEGIN, 0)

        def END(self):
            return self.getToken(TestParser.END, 0)

        def EOF(self):
            return self.getToken(TestParser.EOF, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TestParser.InstructionContext)
            else:
                return self.getTypedRuleContext(TestParser.InstructionContext,i)


        def getRuleIndex(self):
            return TestParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = TestParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(TestParser.BEGIN)
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 15
                self.instruction()
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                    break

            self.state = 20
            self.match(TestParser.END)
            self.state = 21
            self.match(TestParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(TestParser.AssignContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = TestParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.assign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_type(self):
            return self.getTypedRuleContext(TestParser.Variable_typeContext,0)


        def variableId(self):
            return self.getTypedRuleContext(TestParser.VariableIdContext,0)


        def ASSIGN(self):
            return self.getToken(TestParser.ASSIGN, 0)

        def digit(self):
            return self.getTypedRuleContext(TestParser.DigitContext,0)


        def END_OF_INSTRUCTION(self):
            return self.getToken(TestParser.END_OF_INSTRUCTION, 0)

        def getRuleIndex(self):
            return TestParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = TestParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.variable_type()
            self.state = 26
            self.variableId()
            self.state = 27
            self.match(TestParser.ASSIGN)
            self.state = 28
            self.digit()
            self.state = 29
            self.match(TestParser.END_OF_INSTRUCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TestParser.ID, 0)

        def getRuleIndex(self):
            return TestParser.RULE_variableId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableId" ):
                listener.enterVariableId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableId" ):
                listener.exitVariableId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableId" ):
                return visitor.visitVariableId(self)
            else:
                return visitor.visitChildren(self)




    def variableId(self):

        localctx = TestParser.VariableIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(TestParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_type(self):
            return self.getTypedRuleContext(TestParser.Variable_typeContext,0)


        def VOID(self):
            return self.getToken(TestParser.VOID, 0)

        def getRuleIndex(self):
            return TestParser.RULE_value_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_type" ):
                listener.enterValue_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_type" ):
                listener.exitValue_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_type" ):
                return visitor.visitValue_type(self)
            else:
                return visitor.visitChildren(self)




    def value_type(self):

        localctx = TestParser.Value_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value_type)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.variable_type()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(TestParser.VOID)
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


    class Variable_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(TestParser.INTEGER, 0)

        def DOUBLE(self):
            return self.getToken(TestParser.DOUBLE, 0)

        def BOOLEAN(self):
            return self.getToken(TestParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return TestParser.RULE_variable_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_type" ):
                listener.enterVariable_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_type" ):
                listener.exitVariable_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_type" ):
                return visitor.visitVariable_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_type(self):

        localctx = TestParser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
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


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(TestParser.NUMBER, 0)

        def getRuleIndex(self):
            return TestParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigit" ):
                return visitor.visitDigit(self)
            else:
                return visitor.visitChildren(self)




    def digit(self):

        localctx = TestParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(TestParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





