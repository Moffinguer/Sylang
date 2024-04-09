# Generated from Syl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SylParser import SylParser
else:
    from SylParser import SylParser

# This class defines a complete listener for a parse tree produced by SylParser.
class SylListener(ParseTreeListener):

    # Enter a parse tree produced by SylParser#main.
    def enterMain(self, ctx:SylParser.MainContext):
        pass

    # Exit a parse tree produced by SylParser#main.
    def exitMain(self, ctx:SylParser.MainContext):
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


    # Enter a parse tree produced by SylParser#assign.
    def enterAssign(self, ctx:SylParser.AssignContext):
        pass

    # Exit a parse tree produced by SylParser#assign.
    def exitAssign(self, ctx:SylParser.AssignContext):
        pass


    # Enter a parse tree produced by SylParser#variableId.
    def enterVariableId(self, ctx:SylParser.VariableIdContext):
        pass

    # Exit a parse tree produced by SylParser#variableId.
    def exitVariableId(self, ctx:SylParser.VariableIdContext):
        pass


    # Enter a parse tree produced by SylParser#functionId.
    def enterFunctionId(self, ctx:SylParser.FunctionIdContext):
        pass

    # Exit a parse tree produced by SylParser#functionId.
    def exitFunctionId(self, ctx:SylParser.FunctionIdContext):
        pass


    # Enter a parse tree produced by SylParser#functionCall.
    def enterFunctionCall(self, ctx:SylParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SylParser#functionCall.
    def exitFunctionCall(self, ctx:SylParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SylParser#value_type.
    def enterValue_type(self, ctx:SylParser.Value_typeContext):
        pass

    # Exit a parse tree produced by SylParser#value_type.
    def exitValue_type(self, ctx:SylParser.Value_typeContext):
        pass


    # Enter a parse tree produced by SylParser#function_type.
    def enterFunction_type(self, ctx:SylParser.Function_typeContext):
        pass

    # Exit a parse tree produced by SylParser#function_type.
    def exitFunction_type(self, ctx:SylParser.Function_typeContext):
        pass


    # Enter a parse tree produced by SylParser#if_block.
    def enterIf_block(self, ctx:SylParser.If_blockContext):
        pass

    # Exit a parse tree produced by SylParser#if_block.
    def exitIf_block(self, ctx:SylParser.If_blockContext):
        pass


    # Enter a parse tree produced by SylParser#while_block.
    def enterWhile_block(self, ctx:SylParser.While_blockContext):
        pass

    # Exit a parse tree produced by SylParser#while_block.
    def exitWhile_block(self, ctx:SylParser.While_blockContext):
        pass


    # Enter a parse tree produced by SylParser#standard_output.
    def enterStandard_output(self, ctx:SylParser.Standard_outputContext):
        pass

    # Exit a parse tree produced by SylParser#standard_output.
    def exitStandard_output(self, ctx:SylParser.Standard_outputContext):
        pass


    # Enter a parse tree produced by SylParser#expression.
    def enterExpression(self, ctx:SylParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SylParser#expression.
    def exitExpression(self, ctx:SylParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SylParser#variable_type.
    def enterVariable_type(self, ctx:SylParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by SylParser#variable_type.
    def exitVariable_type(self, ctx:SylParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by SylParser#digit.
    def enterDigit(self, ctx:SylParser.DigitContext):
        pass

    # Exit a parse tree produced by SylParser#digit.
    def exitDigit(self, ctx:SylParser.DigitContext):
        pass


    # Enter a parse tree produced by SylParser#boolean_values.
    def enterBoolean_values(self, ctx:SylParser.Boolean_valuesContext):
        pass

    # Exit a parse tree produced by SylParser#boolean_values.
    def exitBoolean_values(self, ctx:SylParser.Boolean_valuesContext):
        pass



del SylParser