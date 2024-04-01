# Generated from Syl.g4 by ANTLR 4.13.1
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
        4,1,44,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,4,1,43,8,1,11,1,12,1,44,1,1,1,1,1,1,1,1,3,1,51,8,1,1,1,1,1,1,
        2,1,2,3,2,57,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,66,8,3,1,4,1,4,
        4,4,70,8,4,11,4,12,4,71,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,3,6,
        83,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,4,10,93,8,10,11,10,12,10,
        94,1,10,1,10,4,10,99,8,10,11,10,12,10,100,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,110,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,5,10,151,8,10,10,10,12,10,154,9,10,1,
        10,0,1,20,11,0,2,4,6,8,10,12,14,16,18,20,0,3,2,0,24,24,29,31,1,0,
        39,41,1,0,43,44,172,0,25,1,0,0,0,2,37,1,0,0,0,4,56,1,0,0,0,6,65,
        1,0,0,0,8,67,1,0,0,0,10,75,1,0,0,0,12,82,1,0,0,0,14,84,1,0,0,0,16,
        86,1,0,0,0,18,88,1,0,0,0,20,109,1,0,0,0,22,24,3,2,1,0,23,22,1,0,
        0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,
        1,0,0,0,28,32,3,8,4,0,29,31,3,2,1,0,30,29,1,0,0,0,31,34,1,0,0,0,
        32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,5,
        0,0,1,36,1,1,0,0,0,37,38,5,27,0,0,38,39,3,12,6,0,39,40,5,38,0,0,
        40,42,5,18,0,0,41,43,3,4,2,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,1,
        0,0,0,44,45,1,0,0,0,45,50,1,0,0,0,46,47,5,33,0,0,47,48,3,20,10,0,
        48,49,5,22,0,0,49,51,1,0,0,0,50,46,1,0,0,0,50,51,1,0,0,0,51,52,1,
        0,0,0,52,53,5,19,0,0,53,3,1,0,0,0,54,57,3,6,3,0,55,57,3,10,5,0,56,
        54,1,0,0,0,56,55,1,0,0,0,57,5,1,0,0,0,58,59,3,14,7,0,59,60,5,38,
        0,0,60,61,5,22,0,0,61,66,1,0,0,0,62,63,3,14,7,0,63,64,3,10,5,0,64,
        66,1,0,0,0,65,58,1,0,0,0,65,62,1,0,0,0,66,7,1,0,0,0,67,69,5,25,0,
        0,68,70,3,4,2,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,
        1,0,0,0,72,73,1,0,0,0,73,74,5,26,0,0,74,9,1,0,0,0,75,76,5,38,0,0,
        76,77,5,17,0,0,77,78,3,20,10,0,78,79,5,22,0,0,79,11,1,0,0,0,80,83,
        3,14,7,0,81,83,5,23,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,13,1,0,0,
        0,84,85,7,0,0,0,85,15,1,0,0,0,86,87,7,1,0,0,87,17,1,0,0,0,88,89,
        7,2,0,0,89,19,1,0,0,0,90,92,6,10,-1,0,91,93,5,20,0,0,92,91,1,0,0,
        0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,98,
        3,20,10,0,97,99,5,21,0,0,98,97,1,0,0,0,99,100,1,0,0,0,100,98,1,0,
        0,0,100,101,1,0,0,0,101,110,1,0,0,0,102,110,5,38,0,0,103,110,3,16,
        8,0,104,110,3,18,9,0,105,106,5,4,0,0,106,110,3,20,10,13,107,108,
        5,16,0,0,108,110,3,20,10,7,109,90,1,0,0,0,109,102,1,0,0,0,109,103,
        1,0,0,0,109,104,1,0,0,0,109,105,1,0,0,0,109,107,1,0,0,0,110,152,
        1,0,0,0,111,112,10,15,0,0,112,113,5,3,0,0,113,151,3,20,10,16,114,
        115,10,14,0,0,115,116,5,4,0,0,116,151,3,20,10,15,117,118,10,12,0,
        0,118,119,5,5,0,0,119,151,3,20,10,13,120,121,10,11,0,0,121,122,5,
        6,0,0,122,151,3,20,10,12,123,124,10,10,0,0,124,125,5,7,0,0,125,151,
        3,20,10,11,126,127,10,9,0,0,127,128,5,14,0,0,128,151,3,20,10,10,
        129,130,10,8,0,0,130,131,5,15,0,0,131,151,3,20,10,9,132,133,10,6,
        0,0,133,134,5,8,0,0,134,151,3,20,10,7,135,136,10,5,0,0,136,137,5,
        9,0,0,137,151,3,20,10,6,138,139,10,4,0,0,139,140,5,10,0,0,140,151,
        3,20,10,5,141,142,10,3,0,0,142,143,5,11,0,0,143,151,3,20,10,4,144,
        145,10,2,0,0,145,146,5,13,0,0,146,151,3,20,10,3,147,148,10,1,0,0,
        148,149,5,12,0,0,149,151,3,20,10,2,150,111,1,0,0,0,150,114,1,0,0,
        0,150,117,1,0,0,0,150,120,1,0,0,0,150,123,1,0,0,0,150,126,1,0,0,
        0,150,129,1,0,0,0,150,132,1,0,0,0,150,135,1,0,0,0,150,138,1,0,0,
        0,150,141,1,0,0,0,150,144,1,0,0,0,150,147,1,0,0,0,151,154,1,0,0,
        0,152,150,1,0,0,0,152,153,1,0,0,0,153,21,1,0,0,0,154,152,1,0,0,0,
        13,25,32,44,50,56,65,71,82,94,100,109,150,152
    ]

class SylParser ( Parser ):

    grammarFileName = "Syl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'#'", "'add'", "'sub'", 
                     "'mul'", "'div'", "'mod'", "'eq'", "'ne'", "'gt'", 
                     "'lt'", "'ge'", "'le'", "'and'", "'or'", "'not'", "':='", 
                     "'{'", "'}'", "'('", "')'", "';'", "'void'", "'int'", 
                     "'BEGIN'", "'END'", "'function'", "'print'", "'string'", 
                     "'boolean'", "'real'", "'if'", "'returns'", "'stop'", 
                     "'next'", "'while'", "'then'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENTS", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULE", "EQUALS", "NOT_EQUALS", "GREATER_THAN", 
                      "LESS_THAN", "GREATER_EQUAL", "LESS_EQUAL", "AND", 
                      "OR", "NOT", "ASSIGN", "OPEN_BLOCK", "CLOSE_BLOCK", 
                      "OPEN_ARGUMENTS", "CLOSE_ARGUMENTS", "END_OF_INSTRUCTION", 
                      "VOID", "INTEGER", "BEGIN", "END", "DEF_FUNC", "ST_OUTPUT", 
                      "STRING", "BOOLEAN", "DOUBLE", "IF", "RETURN", "BREAK", 
                      "CONTINUE", "WHILE", "THEN", "ID", "DECIMAL_NUMBER", 
                      "FLOATING_NUMBER", "HEX_NUMBER", "OCTAL_NUMBER", "TRUE", 
                      "FALSE" ]

    RULE_prog = 0
    RULE_functions = 1
    RULE_instruction = 2
    RULE_var_declaration = 3
    RULE_main = 4
    RULE_var_assign = 5
    RULE_value_type = 6
    RULE_variable_type = 7
    RULE_number = 8
    RULE_boolean_variable = 9
    RULE_expression = 10

    ruleNames =  [ "prog", "functions", "instruction", "var_declaration", 
                   "main", "var_assign", "value_type", "variable_type", 
                   "number", "boolean_variable", "expression" ]

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
    INTEGER=24
    BEGIN=25
    END=26
    DEF_FUNC=27
    ST_OUTPUT=28
    STRING=29
    BOOLEAN=30
    DOUBLE=31
    IF=32
    RETURN=33
    BREAK=34
    CONTINUE=35
    WHILE=36
    THEN=37
    ID=38
    DECIMAL_NUMBER=39
    FLOATING_NUMBER=40
    HEX_NUMBER=41
    OCTAL_NUMBER=42
    TRUE=43
    FALSE=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(SylParser.MainContext,0)


        def EOF(self):
            return self.getToken(SylParser.EOF, 0)

        def functions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SylParser.FunctionsContext)
            else:
                return self.getTypedRuleContext(SylParser.FunctionsContext,i)


        def getRuleIndex(self):
            return SylParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SylParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 22
                self.functions()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.main()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 29
                self.functions()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(SylParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF_FUNC(self):
            return self.getToken(SylParser.DEF_FUNC, 0)

        def value_type(self):
            return self.getTypedRuleContext(SylParser.Value_typeContext,0)


        def ID(self):
            return self.getToken(SylParser.ID, 0)

        def OPEN_BLOCK(self):
            return self.getToken(SylParser.OPEN_BLOCK, 0)

        def CLOSE_BLOCK(self):
            return self.getToken(SylParser.CLOSE_BLOCK, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SylParser.InstructionContext)
            else:
                return self.getTypedRuleContext(SylParser.InstructionContext,i)


        def RETURN(self):
            return self.getToken(SylParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(SylParser.ExpressionContext,0)


        def END_OF_INSTRUCTION(self):
            return self.getToken(SylParser.END_OF_INSTRUCTION, 0)

        def getRuleIndex(self):
            return SylParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = SylParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(SylParser.DEF_FUNC)
            self.state = 38
            self.value_type()
            self.state = 39
            self.match(SylParser.ID)
            self.state = 40
            self.match(SylParser.OPEN_BLOCK)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.instruction()
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 278652780544) != 0)):
                    break

            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 46
                self.match(SylParser.RETURN)
                self.state = 47
                self.expression(0)
                self.state = 48
                self.match(SylParser.END_OF_INSTRUCTION)


            self.state = 52
            self.match(SylParser.CLOSE_BLOCK)
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

        def var_declaration(self):
            return self.getTypedRuleContext(SylParser.Var_declarationContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(SylParser.Var_assignContext,0)


        def getRuleIndex(self):
            return SylParser.RULE_instruction

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

        localctx = SylParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 29, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.var_declaration()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.var_assign()
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


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_type(self):
            return self.getTypedRuleContext(SylParser.Variable_typeContext,0)


        def ID(self):
            return self.getToken(SylParser.ID, 0)

        def END_OF_INSTRUCTION(self):
            return self.getToken(SylParser.END_OF_INSTRUCTION, 0)

        def var_assign(self):
            return self.getTypedRuleContext(SylParser.Var_assignContext,0)


        def getRuleIndex(self):
            return SylParser.RULE_var_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declaration" ):
                listener.enterVar_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declaration" ):
                listener.exitVar_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration" ):
                return visitor.visitVar_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration(self):

        localctx = SylParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declaration)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.variable_type()
                self.state = 59
                self.match(SylParser.ID)
                self.state = 60
                self.match(SylParser.END_OF_INSTRUCTION)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.variable_type()
                self.state = 63
                self.var_assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(SylParser.BEGIN, 0)

        def END(self):
            return self.getToken(SylParser.END, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SylParser.InstructionContext)
            else:
                return self.getTypedRuleContext(SylParser.InstructionContext,i)


        def getRuleIndex(self):
            return SylParser.RULE_main

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

        localctx = SylParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SylParser.BEGIN)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.instruction()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 278652780544) != 0)):
                    break

            self.state = 73
            self.match(SylParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SylParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(SylParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SylParser.ExpressionContext,0)


        def END_OF_INSTRUCTION(self):
            return self.getToken(SylParser.END_OF_INSTRUCTION, 0)

        def getRuleIndex(self):
            return SylParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = SylParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(SylParser.ID)
            self.state = 76
            self.match(SylParser.ASSIGN)
            self.state = 77
            self.expression(0)
            self.state = 78
            self.match(SylParser.END_OF_INSTRUCTION)
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
            return self.getTypedRuleContext(SylParser.Variable_typeContext,0)


        def VOID(self):
            return self.getToken(SylParser.VOID, 0)

        def getRuleIndex(self):
            return SylParser.RULE_value_type

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

        localctx = SylParser.Value_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value_type)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 29, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.variable_type()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(SylParser.VOID)
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
            return self.getToken(SylParser.INTEGER, 0)

        def DOUBLE(self):
            return self.getToken(SylParser.DOUBLE, 0)

        def STRING(self):
            return self.getToken(SylParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(SylParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return SylParser.RULE_variable_type

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

        localctx = SylParser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3774873600) != 0)):
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_NUMBER(self):
            return self.getToken(SylParser.DECIMAL_NUMBER, 0)

        def FLOATING_NUMBER(self):
            return self.getToken(SylParser.FLOATING_NUMBER, 0)

        def HEX_NUMBER(self):
            return self.getToken(SylParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return SylParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = SylParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
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


    class Boolean_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(SylParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SylParser.FALSE, 0)

        def getRuleIndex(self):
            return SylParser.RULE_boolean_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_variable" ):
                listener.enterBoolean_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_variable" ):
                listener.exitBoolean_variable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_variable" ):
                return visitor.visitBoolean_variable(self)
            else:
                return visitor.visitChildren(self)




    def boolean_variable(self):

        localctx = SylParser.Boolean_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolean_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SylParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SylParser.ExpressionContext,i)


        def OPEN_ARGUMENTS(self, i:int=None):
            if i is None:
                return self.getTokens(SylParser.OPEN_ARGUMENTS)
            else:
                return self.getToken(SylParser.OPEN_ARGUMENTS, i)

        def CLOSE_ARGUMENTS(self, i:int=None):
            if i is None:
                return self.getTokens(SylParser.CLOSE_ARGUMENTS)
            else:
                return self.getToken(SylParser.CLOSE_ARGUMENTS, i)

        def ID(self):
            return self.getToken(SylParser.ID, 0)

        def number(self):
            return self.getTypedRuleContext(SylParser.NumberContext,0)


        def boolean_variable(self):
            return self.getTypedRuleContext(SylParser.Boolean_variableContext,0)


        def MINUS(self):
            return self.getToken(SylParser.MINUS, 0)

        def NOT(self):
            return self.getToken(SylParser.NOT, 0)

        def PLUS(self):
            return self.getToken(SylParser.PLUS, 0)

        def MULTIPLY(self):
            return self.getToken(SylParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(SylParser.DIVIDE, 0)

        def MODULE(self):
            return self.getToken(SylParser.MODULE, 0)

        def AND(self):
            return self.getToken(SylParser.AND, 0)

        def OR(self):
            return self.getToken(SylParser.OR, 0)

        def EQUALS(self):
            return self.getToken(SylParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(SylParser.NOT_EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(SylParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(SylParser.LESS_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(SylParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(SylParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return SylParser.RULE_expression

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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SylParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 92 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 91
                        self.match(SylParser.OPEN_ARGUMENTS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 94 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 96
                self.expression(0)
                self.state = 98 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 97
                        self.match(SylParser.CLOSE_ARGUMENTS)

                    else:
                        raise NoViableAltException(self)
                    self.state = 100 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [38]:
                self.state = 102
                self.match(SylParser.ID)
                pass
            elif token in [39, 40, 41]:
                self.state = 103
                self.number()
                pass
            elif token in [43, 44]:
                self.state = 104
                self.boolean_variable()
                pass
            elif token in [4]:
                self.state = 105
                self.match(SylParser.MINUS)
                self.state = 106
                self.expression(13)
                pass
            elif token in [16]:
                self.state = 107
                self.match(SylParser.NOT)
                self.state = 108
                self.expression(7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 150
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 111
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 112
                        self.match(SylParser.PLUS)
                        self.state = 113
                        self.expression(16)
                        pass

                    elif la_ == 2:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 114
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 115
                        self.match(SylParser.MINUS)
                        self.state = 116
                        self.expression(15)
                        pass

                    elif la_ == 3:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 117
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 118
                        self.match(SylParser.MULTIPLY)
                        self.state = 119
                        self.expression(13)
                        pass

                    elif la_ == 4:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 120
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 121
                        self.match(SylParser.DIVIDE)
                        self.state = 122
                        self.expression(12)
                        pass

                    elif la_ == 5:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 124
                        self.match(SylParser.MODULE)
                        self.state = 125
                        self.expression(11)
                        pass

                    elif la_ == 6:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 126
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 127
                        self.match(SylParser.AND)
                        self.state = 128
                        self.expression(10)
                        pass

                    elif la_ == 7:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 129
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 130
                        self.match(SylParser.OR)
                        self.state = 131
                        self.expression(9)
                        pass

                    elif la_ == 8:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 132
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 133
                        self.match(SylParser.EQUALS)
                        self.state = 134
                        self.expression(7)
                        pass

                    elif la_ == 9:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 135
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 136
                        self.match(SylParser.NOT_EQUALS)
                        self.state = 137
                        self.expression(6)
                        pass

                    elif la_ == 10:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 138
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 139
                        self.match(SylParser.GREATER_THAN)
                        self.state = 140
                        self.expression(5)
                        pass

                    elif la_ == 11:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 141
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 142
                        self.match(SylParser.LESS_THAN)
                        self.state = 143
                        self.expression(4)
                        pass

                    elif la_ == 12:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 144
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 145
                        self.match(SylParser.LESS_EQUAL)
                        self.state = 146
                        self.expression(3)
                        pass

                    elif la_ == 13:
                        localctx = SylParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 147
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 148
                        self.match(SylParser.GREATER_EQUAL)
                        self.state = 149
                        self.expression(2)
                        pass

             
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         




