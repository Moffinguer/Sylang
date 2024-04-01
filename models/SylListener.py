# Generated from Syl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SylParser import SylParser
else:
    from SylParser import SylParser

# This class defines a complete listener for a parse tree produced by SylParser.
class SylListener(ParseTreeListener):

    # Enter a parse tree produced by SylParser#prog.
    def enterProg(self, ctx:SylParser.ProgContext):
        pass

    # Exit a parse tree produced by SylParser#prog.
    def exitProg(self, ctx:SylParser.ProgContext):
        pass


    # Enter a parse tree produced by SylParser#functions.
    def enterFunctions(self, ctx:SylParser.FunctionsContext):
        pass

    # Exit a parse tree produced by SylParser#functions.
    def exitFunctions(self, ctx:SylParser.FunctionsContext):
        pass


    # Enter a parse tree produced by SylParser#instruction.
    def enterInstruction(self, ctx:SylParser.InstructionContext):
        pass

    # Exit a parse tree produced by SylParser#instruction.
    def exitInstruction(self, ctx:SylParser.InstructionContext):
        pass


    # Enter a parse tree produced by SylParser#var_declaration.
    def enterVar_declaration(self, ctx:SylParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by SylParser#var_declaration.
    def exitVar_declaration(self, ctx:SylParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by SylParser#main.
    def enterMain(self, ctx:SylParser.MainContext):
        pass

    # Exit a parse tree produced by SylParser#main.
    def exitMain(self, ctx:SylParser.MainContext):
        pass


    # Enter a parse tree produced by SylParser#var_assign.
    def enterVar_assign(self, ctx:SylParser.Var_assignContext):
        pass

    # Exit a parse tree produced by SylParser#var_assign.
    def exitVar_assign(self, ctx:SylParser.Var_assignContext):
        pass


    # Enter a parse tree produced by SylParser#value_type.
    def enterValue_type(self, ctx:SylParser.Value_typeContext):
        pass

    # Exit a parse tree produced by SylParser#value_type.
    def exitValue_type(self, ctx:SylParser.Value_typeContext):
        pass


    # Enter a parse tree produced by SylParser#variable_type.
    def enterVariable_type(self, ctx:SylParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by SylParser#variable_type.
    def exitVariable_type(self, ctx:SylParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by SylParser#number.
    def enterNumber(self, ctx:SylParser.NumberContext):
        pass

    # Exit a parse tree produced by SylParser#number.
    def exitNumber(self, ctx:SylParser.NumberContext):
        pass


    # Enter a parse tree produced by SylParser#boolean_variable.
    def enterBoolean_variable(self, ctx:SylParser.Boolean_variableContext):
        pass

    # Exit a parse tree produced by SylParser#boolean_variable.
    def exitBoolean_variable(self, ctx:SylParser.Boolean_variableContext):
        pass


    # Enter a parse tree produced by SylParser#expression.
    def enterExpression(self, ctx:SylParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SylParser#expression.
    def exitExpression(self, ctx:SylParser.ExpressionContext):
        pass



del SylParser