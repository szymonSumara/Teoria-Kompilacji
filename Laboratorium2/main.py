import sys
from lexer import Lexer
import my_parser

#
# args = sys.argv[1:]
#
# if not args:
#     print('\033[91m' + '[ERROR] : No file path provided')
#     exit(1)
#
#
# try:
#     data = open(args[0], "r").read()
# except FileNotFoundError:
#     print('\033[91m' + '[ERROR] : File "' + args[0] + '" found')
#     exit()


data = 'N = 10;' \
       'M = 20;' \
 \
    'if(N==10)' \
    'print "N==10";' \
    'else if(N!=10)' \
    'print "N!=10";' \
 \
    'if(N>5) {' \
    'print "N>5";' \
    '}' \
    'else if(N>=0) {' \
    'print "N>=0";' \
    '}' \
 \
    'if(N<10) {' \
    'print "N<10";' \
    '}' \
    'else if(N<=15)' \
    'print "N<=15";'

lexer = Lexer()
lexer.tokenize(data)

tokens = lexer.getTokens()

print(tokens)

our_parser = my_parser.build_parser()
our_parser.parse(data, lexer.lexer)
