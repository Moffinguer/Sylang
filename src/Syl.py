import sys
from antlr4 import *
from SylLexer import SylLexer
from SylParser import SylParser
from VisitorInterp import VisitorInterp


def main(argv):
    input = FileStream(argv[1])
    lexer = SylLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SylParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp()
        vinterp.visit(tree)


if __name__ == '__main__':
    main(sys.argv)