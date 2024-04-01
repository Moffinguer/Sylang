import sys
from antlr4 import *
from TestLexer import TestLexer
from TestParser import TestParser
from VisitorInterp import VisitorInterp


def main(argv):
    input = FileStream(argv[1])
    lexer = TestLexer(input)
    stream = CommonTokenStream(lexer)
    parser = TestParser(stream)
    tree = parser.main()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp()
        vinterp.visit(tree)


if __name__ == '__main__':
    main(sys.argv)