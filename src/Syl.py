import sys
from antlr4 import *
from SylLexer import SylLexer
from SylParser import SylParser
from VisitorInterp import VisitorInterp


def format_code_with_clang_format(code):
    import shutil
    import subprocess
    if shutil.which('clang-format'):
        process = subprocess.Popen(['clang-format'], 
                                   stdin=subprocess.PIPE, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE, 
                                   universal_newlines=True)
        
        formatted_code, error = process.communicate(code)
        
        return formatted_code
    else:
        return code

def main(argv):
    input = FileStream(argv[1])
    #input = FileStream("src/test.syl")
    lexer = SylLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SylParser(stream)
    tree = parser.main()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp()
        vinterp.visit(tree)
        error_msg = vinterp.get_error()
        if error_msg == "":
            with open(argv[1].replace(".syl",".c"), "w") as file:
                file.write(format_code_with_clang_format(vinterp.get_output()))
        else:
            print(error_msg)

if __name__ == '__main__':
    main(sys.argv)