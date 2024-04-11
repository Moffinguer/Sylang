import sys
from antlr4 import *
from SylLexer import SylLexer
from SylParser import SylParser
from VisitorInterp import VisitorInterp
from Helpers import ErrorControl
from SyntaxErrors import CustomSyntaxError

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

    if len(argv) == 1:
        print(ErrorControl.noFileLoaded())
        sys.exit(1)
    elif argv[1].split(".")[1] != "syl":
        print(ErrorControl.wrongFileExtension(argv[1]))
        sys.exit(2)

    input = FileStream(argv[1])
    lexer = SylLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SylParser(stream)

    error_listener = CustomSyntaxError()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.main()
    if parser.getNumberOfSyntaxErrors() == 0:
        vinterp = VisitorInterp()
        vinterp.visit(tree)
        error_msg = vinterp.get_error()
        if error_msg == "":
            with open(argv[1].replace(".syl",".c"), "w") as file:
                file.write(format_code_with_clang_format(vinterp.get_output()))
            sys.exit(0)
        else:
            print(error_msg)
            sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)