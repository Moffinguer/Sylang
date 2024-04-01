import sys
from antlr4 import *
from TestParser import TestParser
from TestVisitor import TestVisitor


class HelperTranslator():
    translator = {
        "BEGIN": { "c_translation": "int main() { \\\\BEGIN MAIN", "indent": 1 },
        "END": { "c_translation": "\treturn 0;\n} \\\\END MAIN", "indent": -1 },
        ":=": { "c_translation": "=", "indent": 0},
        ";": { "c_translation": ";", "indent": 0},
        "int": { "c_translation": "int", "indent": 0},
        "real": { "c_translation": "double", "indent": 0},
        "boolean": { "c_translation": "int", "indent": 0},
    }


class VisitorInterp(TestVisitor):

    def __init__(self):
        super().__init__()
        self.indent = 0
        self.translator = HelperTranslator.translator
        self.output = ""
        self.last_type = ""
        self.is_assign = False
        self.used_variables = {}

    def set_indent(self, indent):
        self.indent += indent

    def set_newline(self):
        self.output += "\n"
    
    def visitMain(self, ctx:TestVisitor.visitMain):       
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            if node.getChildCount() == 0:
                try:
                    transform = self.translator[node.getText()]
                    self.set_indent(transform["indent"])
                    self.output += transform["c_translation"]
                    self.set_newline()
                except KeyError:
                    self.output += ""
            self.visit(ctx.getChild(i))
        print(self.output)

    def visitInstruction(self, ctx:TestVisitor.visitInstruction):
        self.output += "" + self.indent*"\t"
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            if node.getChildCount() == 0:
                next
            self.visit(ctx.getChild(i))
        self.set_newline()

    def visitAssign(self, ctx:TestVisitor.visitAssign):
        self.output += "" + self.indent*"\t"
        self.is_assign = True
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            if node.getChildCount() == 0:
                try:
                    transform = self.translator[node.getText()]
                    self.output += transform["c_translation"]
                except KeyError:
                    self.output += node.getText()
                next
            self.visit(ctx.getChild(i))
        self.set_newline()
        self.is_assign = False

    def visitDigit(self, ctx:TestVisitor.visitDigit):
        digit = ""
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            digit += node.getText()
        self.output += digit

    def visitVariable_type(self, ctx:TestVisitor.visitVariable_type):
        transform = self.translator[ctx.getChild(0).getText()]
        self.output += transform["c_translation"] + " "

        if self.is_assign:
            self.last_type = transform["c_translation"]

    def visitVariableId(self, ctx:TestVisitor.visitVariableId):
        variable = ctx.getText()
        self.output += variable + " "
        
        if self.is_assign:
            self.used_variables[variable] = { "type": self.last_type }

    # VisitExpression