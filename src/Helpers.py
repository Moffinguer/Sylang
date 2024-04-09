

import re
def evaluateExpression(expression, vars = {}):

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
            return "int"
        except:
            pass
    try:
        float(expression)
        return "double"
    except:
        pass
    
    expression = re.sub(r'\s+', ' ', expression.strip())
    evaluated_expression = eval(expression)
    if isinstance(evaluated_expression, bool) or isinstance(evaluated_expression, int):
        return "int"
    elif isinstance(evaluated_expression, float):
        return "double"

    return "error"


from colorama import Fore, Style
class ErrorControl():
    def __init__(self, line, column, message):
        self.line = line
        self.column = column
        self.message = message
    def __str__(self):
        error_msg = f"<{Fore.RED}{self.message}{Style.RESET_ALL}>\n"
        error_msg += f"{Fore.BLUE}line:{Fore.RESET} {self.line} "
        error_msg += f"{Fore.GREEN}column:{Fore.RESET} {self.column}"
        return error_msg

class HelperTranslator():
    translator = {
        "BEGIN": { "c_translation": "int main() {", "indent": 1 },
        "END": { "c_translation": "\treturn 0;\n}", "indent": -1 },
        ":=": { "c_translation": "=", "indent": 0},
        ";": { "c_translation": ";", "indent": 0},
        "int": { "c_translation": "int", "indent": 0},
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
    }
