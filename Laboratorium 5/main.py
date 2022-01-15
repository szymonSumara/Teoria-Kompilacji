import sys
from lexer import Lexer
import my_parser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/print.m"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/control_transfer.m"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/opers.m"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/init.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    lexer = Lexer()
    our_parser = my_parser.build_parser(lexer.lexer)
    ast = our_parser.parse(file.read(), lexer.lexer)
    if not my_parser.HAVE_ERRORS:
        ast.printTree()

        # Below code shows how to use visitor
        typeChecker = TypeChecker()
        typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)
        ast.accept(Interpreter())