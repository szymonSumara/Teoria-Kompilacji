import sys
from lexer import Lexer
import my_parser
from TreePrinter import TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    lexer = Lexer()
    our_parser = my_parser.build_parser()
    ast = our_parser.parse(file.read(), lexer.lexer)
    if not my_parser.HAVE_ERRORS:
        ast.printTree()