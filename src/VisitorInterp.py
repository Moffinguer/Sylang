import sys
from antlr4 import *
from SylParser import SylParser
from SylVisitor import SylVisitor

class VisitorInterp(SylVisitor):

    def visitProg(self, ctx:SylParser.ProgContext):
        for i in range(0, ctx.getChildCount()):
            print(self.visit(ctx.getChild(i)))

    def visitMain(self, ctx:SylParser.MainContext):
        print(ctx.getChild(0).getText())

        for i in range(1, ctx.getChildCount()-1):
            print(self.visit(ctx.getChild(i)))

        print(ctx.getChild(ctx.getChildCount()-1).getText())

    def visitFunctions(self, ctx:SylParser.FunctionsContext):
        for i in range(0, ctx.getChildCount()):
            print(self.visit(ctx.getChild(i)))

    def visitInstruction(self, ctx:SylParser.InstructionContext):
        for i in range(0, ctx.getChildCount()):
            print(self.visit(ctx.getChild(i)))

    def visitVar_assign(self, ctx:SylParser.Var_assignContext):
        for i in range(0, ctx.getChildCount()):
            print(self.visit(ctx.getChild(i)))

    def visitExpression(self, ctx:SylParser.ExpressionContext):
        for i in range(0, ctx.getChildCount()):
            print(ctx.getChild(i).getText())

    def visitVar_declaration(self, ctx:SylParser.Var_declarationContext):
        for i in range(0, ctx.getChildCount()):
            print(ctx.getChild(i).getText())
    
    