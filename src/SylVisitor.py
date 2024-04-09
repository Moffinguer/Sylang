# Generated from Syl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SylParser import SylParser
else:
    from SylParser import SylParser

# This class defines a complete generic visitor for a parse tree produced by SylParser.

class SylVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SylParser#main.
    def visitMain(self, ctx:SylParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#functions.
    def visitFunctions(self, ctx:SylParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#instruction.
    def visitInstruction(self, ctx:SylParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#assign.
    def visitAssign(self, ctx:SylParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#variableId.
    def visitVariableId(self, ctx:SylParser.VariableIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#functionId.
    def visitFunctionId(self, ctx:SylParser.FunctionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#functionCall.
    def visitFunctionCall(self, ctx:SylParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#value_type.
    def visitValue_type(self, ctx:SylParser.Value_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#function_type.
    def visitFunction_type(self, ctx:SylParser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#if_block.
    def visitIf_block(self, ctx:SylParser.If_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#while_block.
    def visitWhile_block(self, ctx:SylParser.While_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#standard_output.
    def visitStandard_output(self, ctx:SylParser.Standard_outputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#expression.
    def visitExpression(self, ctx:SylParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#variable_type.
    def visitVariable_type(self, ctx:SylParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#digit.
    def visitDigit(self, ctx:SylParser.DigitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#boolean_values.
    def visitBoolean_values(self, ctx:SylParser.Boolean_valuesContext):
        return self.visitChildren(ctx)



del SylParser