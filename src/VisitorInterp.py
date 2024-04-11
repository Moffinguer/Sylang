import sys
from antlr4 import *
from SylParser import SylParser
from SylVisitor import SylVisitor
from Helpers import HelperTranslator, evaluateExpression, ErrorControl


class VisitorInterp(SylVisitor):

    def __init__(self):
        super().__init__()
        self.indent = 0
        self.translator = HelperTranslator.translator
        self.output = ""
        self.last_type = ""
        self.last_variable = ""
        self.is_assign = False
        self.is_function = False
        self.used_variables = {}
        self.last_expression = ""
        self.error = ""
        self.used_functions = {}
        self.vars_in_function = {}
        self.is_function = False
        self.last_original_expression = ""
        self.is_print = True

    def set_indent(self, indent):
        self.indent += indent

    def set_newline(self):
        self.output += "\n"
    
    def get_output(self):
        return self.output

    def get_error(self):
        return self.error

    def visitMain(self, ctx:SylVisitor.visitMain):       
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
        self.error = self.error.strip()

    def visitInstruction(self, ctx:SylVisitor.visitInstruction):
        self.output += "" + self.indent*"\t"
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            if node.getChildCount() == 0:
                next
            self.visit(ctx.getChild(i))
        self.set_newline()

    def visitStandard_output(self, ctx:SylVisitor.visitStandard_output):
        self.output += "" + self.indent*"\t" + f"printf({ctx.getChild(2)});" 
        if self.is_print:
            self.output = "#include <stdio.h>\n" + self.output
            self.is_print = False
        self.set_newline()

    def visitAssign(self, ctx:SylVisitor.visitAssign):
        self.output += "" + self.indent*"\t"
        self.last_variable = ""
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
        if self.last_expression != "":
            start = ctx.start
            
            if not self.is_function:
                type_expression, error = evaluateExpression(self.last_expression, self.used_variables, self.error,start.line, start.column, self.used_functions  )
            else:
                type_expression, error = evaluateExpression(self.last_expression, self.vars_in_function, self.error,start.line, start.column, self.used_functions  )

            self.error = error
            if not self.is_function:
                if type_expression != self.used_variables[self.last_variable]["type"] or ( self.used_variables[self.last_variable]["type"] == "int" and type_expression == "real"):
                    self.error += ErrorControl(start.line, start.column, f"Expected a {self.translator[self.used_variables[self.last_variable]['type']]['syl_translation']} expression. Got a {self.translator[type_expression]['syl_translation']} instead",  f"{self.last_original_expression}").__str__()
                self.used_variables[self.last_variable]["value_type"] = type_expression
            else:
                if type_expression != self.vars_in_function[self.last_variable]["type"] and ( self.vars_in_function[self.last_variable]["type"] == "int" and type_expression == "real"):
                    self.error += ErrorControl(start.line, start.column, f"Expected a {self.translator[self.vars_in_function[self.last_variable]['type']]['syl_translation']} expression. Got a {self.translator[type_expression]['syl_translation']} instead",  f"{self.last_original_expression}").__str__()
                self.vars_in_function[self.last_variable]["value_type"] = type_expression

            self.error += "\n"
            self.last_expression = ""
            self.last_original_expression = ""
        self.set_newline()
        self.is_assign = False

    def visitExpression(self, ctx:SylVisitor.visitExpression):
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            if node.getChildCount() not in [0,1]:
                self.visit(node)
                continue
            if self.is_assign:
                if node.getText() in self.translator:
                    self.output += " " + self.translator[node.getText()]["c_translation"] + " "
                    self.last_expression += " " + self.translator[node.getText()]["c_translation"] + " "
                else:
                    self.output += " " + node.getText() + " "
                    self.last_expression += " " + node.getText() + " "
            else:
                if node.getText() in self.translator:
                    self.last_expression += " " + self.translator[node.getText()]["c_translation"] + " "
                else:
                    self.last_expression += " " + node.getText() + " "
            self.last_original_expression += " " + node.getText() + " "

    def visitDigit(self, ctx:SylVisitor.visitDigit):
        digit = ""
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            digit += node.getText()
        self.output += digit
        self.last_expression += digit
        self.last_original_expression += " " + digit + " "

    def visitBoolean_values(self, ctx:SylVisitor.visitBoolean_values):
        boolean_value = ""
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            boolean_value += " " + self.translator[node.getText()]["c_translation"] + " "
            self.last_original_expression += " " + node.getText() + " "
        self.output += boolean_value
        self.last_expression += boolean_value

    def visitVariable_type(self, ctx:SylVisitor.visitVariable_type):
        transform = self.translator[ctx.getChild(0).getText()]
        self.output += transform["c_translation"] + " "

        if self.is_assign:
            self.last_type = transform["c_translation"]

    def visitVariableId(self, ctx:SylVisitor.visitVariableId):
        variable = ctx.getText()
        self.output += variable + " "
        
        if self.is_assign:
            if self.is_function:
                if variable not in self.vars_in_function and variable not in self.used_functions:   
                    self.vars_in_function[variable] = { "type": self.last_type }
                    self.last_variable = variable
                else:
                    if variable in self.vars_in_function:
                        self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Variable {variable} is already defined", "").__str__()
                    else:
                        self.error += ErrorControl(ctx.start.line, ctx.start.column, f"A function {variable} with the same name is already defined.", "").__str__()        
            else:
                if variable not in self.used_variables and variable not in self.used_functions:   
                    self.used_variables[variable] = { "type": self.last_type }
                    self.last_variable = variable
                else:
                    if variable in self.used_variables:
                        self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Variable {variable} is already defined", "").__str__()
                    else:
                        self.error += ErrorControl(ctx.start.line, ctx.start.column, f"A function {variable} with the same name is already defined.", "").__str__()                    
    
    def visitIf_block(self, ctx:SylVisitor.visitIf_block):
        self.output += "" + self.indent*"\t" + f"if( "
        self.visit(ctx.getChild(1))
        start = ctx.start
        if not self.is_function:
            type_condition, error = evaluateExpression(self.last_expression, self.used_variables, self.error,start.line, start.column, self.used_functions )
        else:
            type_condition, error = evaluateExpression(self.last_expression, self.vars_in_function, self.error,start.line, start.column, self.used_functions )
        self.error = error
        if type_condition != "int":
            self.error += ErrorControl(start.line, start.column, f"Expected a conditional statement", f" if {self.last_original_expression} then").__str__()
            self.error += "\n"
        self.output += self.last_expression + " ){"
        self.set_newline()
        self.last_expression = ""
        self.last_original_expression = ""
        for i in range(3, ctx.getChildCount()):
            node = ctx.getChild(i)
            if node.getText() in self.translator:
                if node.getText() == "else":
                    self.output += "\n" + self.indent*"\t" + "} else {"
                    self.set_newline()
                elif node.getText() == "fi":
                    self.output += "\n" + self.indent*"\t" + "}"
                    self.set_newline()
                elif node.getText() == "then":
                    self.output += "\n" + self.indent*"\t" + "{"
                    self.set_newline()
            else:
                self.last_expression = ""
                self.last_original_expression = ""
                self.visit(ctx.getChild(i))
                self.last_expression = ""
                self.last_original_expression = ""

    def visitWhile_block(self, ctx:SylVisitor.visitWhile_block):
        self.output += "" + self.indent*"\t" + f"while( "
        self.visit(ctx.getChild(1))
        start = ctx.start
        if not self.is_function:
            type_condition, error = evaluateExpression(self.last_expression, self.used_variables, self.error,start.line, start.column, self.used_functions  )
        else:
            type_condition, error = evaluateExpression(self.last_expression, self.vars_in_function, self.error,start.line, start.column, self.used_functions  )        
        self.error = error
        
        if type_condition != "int":
            self.error += ErrorControl(start.line, start.column, f"Expected a conditional statement",  f" while {self.last_original_expression} then").__str__()
            self.error += "\n"
        self.output += self.last_expression + " ){"
        self.set_newline()
        self.last_expression = ""
        self.last_original_expression = ""
        for i in range(3, ctx.getChildCount()):
            node = ctx.getChild(i)
            if node.getText() in self.translator:
                if node.getText() == "then":
                    self.output += "\n" + self.indent*"\t" + "{"
                    self.set_newline()
                elif node.getText() == "end":
                    self.output += "\n" + self.indent*"\t" + "}"
                    self.set_newline()
            else:
                self.last_expression = ""
                self.last_original_expression = ""
                self.visit(ctx.getChild(i))
                self.last_expression = ""
                self.last_original_expression = ""

    def visitFunctions(self, ctx:SylVisitor.visitFunctions):
        function_definition = self.translator[ctx.getChild(0).getText()]["c_translation"]
        type_definition = self.translator[ctx.getChild(1).getText()]["c_translation"]
        function_name = ctx.getChild(2).getText()
        if function_name in self.used_functions:
            self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Function {function_name} is already defined", "").__str__()
        else:
            self.used_functions[function_name] = { "type": type_definition }

        instruccion_sets = 3
        self.output += function_definition + " " + type_definition + " " + function_name + "("
        self.is_function = True
        self.used_functions[function_name]["arguments"] = []
        if ctx.getChild(4).getText() != ")":
            for i in range(4, ctx.getChildCount(),3):
                arg_type = ctx.getChild(i)
                arg_var_name = ctx.getChild(i + 1)
                last_element = ctx.getChild(i + 2)                  
                self.used_functions[function_name]["arguments"] += [{"arg_name": arg_var_name.getText(), "type": arg_type.getText()}]
                self.vars_in_function[arg_var_name.getText()] = { "type": arg_type.getText() }
                self.output += arg_type.getText() + " " + arg_var_name.getText()

                if not len(self.used_functions[function_name]["arguments"]) == 1 and len([function for function in self.used_functions[function_name]["arguments"] if function["arg_name"] == arg_var_name.getText()]) > 1:
                    self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Argument {arg_var_name.getText()} is already defined", "").__str__()                    

                instruccion_sets += 2

                if last_element.getText() == ",":
                    self.output += ", "
                    instruccion_sets += 1
                
                if last_element.getText() == ")":
                    break
        

        self.output += "){"
        instruccion_sets += 2
        self.set_newline()
        for i in range(instruccion_sets, ctx.getChildCount() - 1):
            self.visit(ctx.getChild(i))
            if ctx.getChild(i).getText() == "returns":
                self.output += "return "
                self.visit(ctx.getChild(i + 1))
                self.output += ";"
                break
        self.output += "}\n\n"
        self.is_function = False
        #self.last_variable = ""
        self.last_original_expression = ""
        self.last_type = ""
        self.last_expression = ""

    def visitFunction_type(self, ctx:SylVisitor.visitFunction_type):
        pass

    def visitFunctionId(self, ctx:SylVisitor.visitFunctionId):
        self.output += " " + ctx.getChild(0).getText()

    def visitFunctionCall(self, ctx:SylVisitor.visitFunctionCall):
        function_name = ctx.getChild(0).getText()
        self.visit(ctx.getChild(0))

        function_arguments = []

        self.output += "("
        for i in range(2, ctx.getChildCount() - 1):
            arg = ctx.getChild(i)
            if arg.getText() == ",":
                self.output += ", "
                continue

            if self.is_function:
                if arg.getText() not in self.vars_in_function and not (isinstance(eval(arg.getText()), int) or isinstance(eval(arg.getText()), float)):
                    self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Variable {arg.getText()} is not defined", "").__str__()
            else:
                if arg.getText() not in self.used_variables and not (isinstance(eval(arg.getText()), int) or isinstance(eval(arg.getText()), float)):
                    self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Variable {arg.getText()} is not defined", "").__str__()
            self.output += arg.getText()
            function_arguments += [arg.getText()]
        
        try:
            for argument_index in range(len(self.used_functions[function_name]["arguments"])):
                if self.is_function:
                    evaluated_type, error =evaluateExpression(function_arguments[argument_index], self.vars_in_function, self.error, ctx.start.line, ctx.start.column, self.used_functions)
                else:
                    evaluated_type, error =evaluateExpression(function_arguments[argument_index], self.used_variables, self.error, ctx.start.line, ctx.start.column, self.used_functions)
                
                self.error += error

                if self.used_functions[function_name]["arguments"][argument_index]["type"] != evaluated_type:
                    self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Parameter {arg.getText()} is not of type {self.translator[evaluated_type]['syl_translation']}", "").__str__()
        except:
            self.error += ErrorControl(ctx.start.line, ctx.start.column, f"Function {function_name} is not defined", "").__str__()

        self.output += ")"