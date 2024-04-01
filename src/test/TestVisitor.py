# Generated from Test.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete generic visitor for a parse tree produced by TestParser.

class TestVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestParser#main.
    def visitMain(self, ctx:TestParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#instruction.
    def visitInstruction(self, ctx:TestParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#assign.
    def visitAssign(self, ctx:TestParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#variableId.
    def visitVariableId(self, ctx:TestParser.VariableIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#value_type.
    def visitValue_type(self, ctx:TestParser.Value_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#variable_type.
    def visitVariable_type(self, ctx:TestParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#digit.
    def visitDigit(self, ctx:TestParser.DigitContext):
        return self.visitChildren(ctx)



del TestParser