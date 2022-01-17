import sys
from lexer import Lexer
import my_parser
from TreePrinter import TreePrinter
import TypeChecker
from Interpreter import Interpreter
from Exceptions import ReturnValueException

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/Interpreter/fibonacci.m"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/Interpreter/matrix.m"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/Interpreter/pi.m"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/Interpreter/primes.m"
        #filename = sys.argv[1] if len(sys.argv) > 1 else "./Examples/Interpreter/triangle.m"


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
        typeChecker = TypeChecker.TypeChecker()
        typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)
        if TypeChecker.HAVE_ERRORS:
            print("have errors")
        else:
            try:
                ast.accept(Interpreter())
            except ReturnValueException as return_value:
                print("Program return: " + str(return_value))