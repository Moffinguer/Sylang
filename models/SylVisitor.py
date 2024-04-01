# Generated from Syl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SylParser import SylParser
else:
    from SylParser import SylParser

# This class defines a complete generic visitor for a parse tree produced by SylParser.

class SylVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SylParser#prog.
    def visitProg(self, ctx:SylParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#functions.
    def visitFunctions(self, ctx:SylParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#instruction.
    def visitInstruction(self, ctx:SylParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#var_declaration.
    def visitVar_declaration(self, ctx:SylParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#main.
    def visitMain(self, ctx:SylParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#var_assign.
    def visitVar_assign(self, ctx:SylParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#value_type.
    def visitValue_type(self, ctx:SylParser.Value_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#variable_type.
    def visitVariable_type(self, ctx:SylParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#number.
    def visitNumber(self, ctx:SylParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#boolean_variable.
    def visitBoolean_variable(self, ctx:SylParser.Boolean_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SylParser#expression.
    def visitExpression(self, ctx:SylParser.ExpressionContext):
        return self.visitChildren(ctx)



del SylParser