import re
def evaluateExpression(expression, vars = {}, errors = "", line = 0, column = 0):
    if vars:
        for variable in vars.keys():
            var_type = vars[variable]["type"]
            if var_type == "int":
                expression = expression.replace(variable, "1")
            elif var_type == "double":
                expression = expression.replace(variable, "1.0") 

    for base in [2,10,16]:
        try:
            int(expression, base)
            return "int", errors
        except:
            pass
    try:
        float(expression)
        return "double", errors
    except:
        pass
    
    expression = re.sub(r'\s+', ' ', expression.strip())

    sub_term = ""
    for operator in ["%", "&&", "||", "!"]:
        if operator in expression:
            indexes = []
            position = expression.find(operator)
            while position != -1:
                indexes.append(position)
                position = expression.find(operator, position+1)
            sub_term = ""
            for index in indexes:
                left_member, right_member = (expression[:index], expression[index+2:])
                for term in right_member.split():
                    if isinstance(eval(term), float):
                        errors += ErrorControl(line, column, f"Cannot evaluate expression with real number", f" ...{HelperTranslator.translator[operator]['syl_translation']} {term}").__str__()
                        break
                    if sub_term == "" and (isinstance(eval(term), int) or isinstance(eval(term), bool)):
                        break 

                    if ")" in term:
                        open_parentesis = sub_term.count("(")
                        sub_term += term
                        close_parentesis = sub_term.count(")")
                        if (open_parentesis - close_parentesis) == 0:
                            if isinstance(eval(sub_term), float):
                                errors += ErrorControl(line, column, f"Cannot evaluate expression with real number", f" ...{HelperTranslator.translator[operator]['syl_translation']} {sub_term}").__str__()
                            break
                        continue
                    sub_term += term
                if operator != "!":
                    sub_term = ""
                    for term in left_member.split()[::-1]:
                        if isinstance(eval(term), float):
                            errors += ErrorControl(line, column, f"Cannot evaluate expression with real number", f" {term} {HelperTranslator.translator[operator]['syl_translation']}...").__str__()
                            break
                        if sub_term == "" and (isinstance(eval(term), int) or isinstance(eval(term), bool)):
                            break
                        if "(" in term:
                            open_parentesis = sub_term.count(")")
                            sub_term += term
                            close_parentesis = sub_term.count("(")
                            if (open_parentesis - close_parentesis) == 0:
                                if isinstance(eval(sub_term), float):
                                    errors += ErrorControl(line, column, f"Cannot evaluate expression with real number", f" {sub_term} {HelperTranslator.translator[operator]['syl_translation']}...").__str__()
                                break
                            continue
                        sub_term += term


    try:
        for i in ["&&", "||", "!"]:
            expression = expression.replace(i, HelperTranslator.translator[i]["syl_translation"])
        evaluated_expression = eval(expression)
        if isinstance(evaluated_expression, bool) or isinstance(evaluated_expression, int):
            return "int", errors
        elif isinstance(evaluated_expression, float):
            return "double", errors
    except ZeroDivisionError:
        errors += ErrorControl(line, column, f"Cannot divide by zero", "... div ...").__str__()

    return "error", errors


from colorama import Fore, Style
class ErrorControl():
    def __init__(self, line, column, message, expression):
        self.line = line
        self.column = column
        self.message = message
        self.expression = expression
    def __str__(self):
        error_msg = f"{Style.BRIGHT}{Fore.YELLOW}{self.expression}{Style.RESET_ALL}"
        error_msg += f" {Fore.MAGENTA}<~{Style.RESET_ALL}"
        error_msg += f" <{Fore.RED}{self.message}{Style.RESET_ALL}>\n"
        error_msg += f"{Fore.BLUE}line:{Fore.RESET} {self.line} "
        error_msg += f"{Fore.GREEN}column:{Fore.RESET} {self.column}"
        return error_msg

    def noFileLoaded():
        error_msg = f"{Style.BRIGHT}{Fore.YELLOW}No input received{Style.RESET_ALL}"
        return error_msg
    
    def wrongFileExtension(file_name):
        error_msg = f"{Style.BRIGHT}{Fore.YELLOW}File '{file_name}' is not a .syl file{Style.RESET_ALL}"
        return error_msg
class HelperTranslator():
    translator = {
        "BEGIN": { "c_translation": "int main() {", "indent": 1 },
        "END": { "c_translation": "\treturn 0;\n}", "indent": -1 },
        ":=": { "c_translation": "=", "indent": 0},
        ";": { "c_translation": ";", "indent": 0},
        "int": { "c_translation": "int", "indent": 0, "syl_translation": "int",},
        "real": { "c_translation": "double", "indent": 0},
        "boolean": { "c_translation": "int", "indent": 0},
        "gt": { "c_translation": ">", "indent": 0},
        "lt": { "c_translation": "<", "indent": 0},
        "ge": { "c_translation": ">=", "indent": 0},
        "le": { "c_translation": "<=", "indent": 0},
        "ne": { "c_translation": "!=", "indent": 0},
        "eq": { "c_translation": "==", "indent": 0},
        "add": { "c_translation": "+", "indent": 0},
        "sub": { "c_translation": "-", "indent": 0},
        "mul": { "c_translation": "*", "indent": 0},
        "div": { "c_translation": "/", "indent": 0},
        "mod": { "c_translation": "%", "indent": 0},
        "and": { "c_translation": "&&", "indent": 0},
        "or": { "c_translation": "||", "indent": 0},
        "not": { "c_translation": "!", "indent": 0},
        ",": { "c_translation": ",", "indent": 0},
        "{": { "c_translation": "{", "indent": 1},
        "}": { "c_translation": "}", "indent": -1},
        "(": { "c_translation": "(", "indent": 0},
        ")": { "c_translation": ")", "indent": 0},
        "void": { "c_translation": "void", "indent": 0},
        "function": { "c_translation": "", "indent": 0},
        "print": { "c_translation": "printf", "indent": 0},
        "returns": { "c_translation": "return", "indent": 0},
        "while": { "c_translation": "while", "indent": 0},
        "then": { "c_translation": "{", "indent": 1},
        "else": { "c_translation": "else", "indent": 0},
        "fi": { "c_translation": "}", "indent": -1},
        "end": { "c_translation": "}", "indent": -1},
        "T": { "c_translation": "1", "indent": 0},
        "TRUE": { "c_translation": "1", "indent": 0},
        "FALSE": { "c_translation": "0", "indent": 0},
        "F": { "c_translation": "0", "indent": 0},
        "double": { "syl_translation": "real", "indent": 0},
        "error": { "syl_translation": "none", "indent": 0},
        "&&": { "syl_translation": "and", "indent": 0},
        "||": { "syl_translation": "or", "indent": 0},
        "%": { "syl_translation": "mod", "indent": 0},
        "!": { "syl_translation": "not", "indent": 0}
    }
