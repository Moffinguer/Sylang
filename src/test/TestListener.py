# Generated from Test.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete listener for a parse tree produced by TestParser.
class TestListener(ParseTreeListener):

    # Enter a parse tree produced by TestParser#main.
    def enterMain(self, ctx:TestParser.MainContext):
        pass

    # Exit a parse tree produced by TestParser#main.
    def exitMain(self, ctx:TestParser.MainContext):
        pass


    # Enter a parse tree produced by TestParser#instruction.
    def enterInstruction(self, ctx:TestParser.InstructionContext):
        pass

    # Exit a parse tree produced by TestParser#instruction.
    def exitInstruction(self, ctx:TestParser.InstructionContext):
        pass


    # Enter a parse tree produced by TestParser#assign.
    def enterAssign(self, ctx:TestParser.AssignContext):
        pass

    # Exit a parse tree produced by TestParser#assign.
    def exitAssign(self, ctx:TestParser.AssignContext):
        pass


    # Enter a parse tree produced by TestParser#variableId.
    def enterVariableId(self, ctx:TestParser.VariableIdContext):
        pass

    # Exit a parse tree produced by TestParser#variableId.
    def exitVariableId(self, ctx:TestParser.VariableIdContext):
        pass


    # Enter a parse tree produced by TestParser#value_type.
    def enterValue_type(self, ctx:TestParser.Value_typeContext):
        pass

    # Exit a parse tree produced by TestParser#value_type.
    def exitValue_type(self, ctx:TestParser.Value_typeContext):
        pass


    # Enter a parse tree produced by TestParser#variable_type.
    def enterVariable_type(self, ctx:TestParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by TestParser#variable_type.
    def exitVariable_type(self, ctx:TestParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by TestParser#digit.
    def enterDigit(self, ctx:TestParser.DigitContext):
        pass

    # Exit a parse tree produced by TestParser#digit.
    def exitDigit(self, ctx:TestParser.DigitContext):
        pass



del TestParser