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


data = '1.0 - 20. + 6 6 + 3.'

lexer = Lexer()
lexer.tokenize(data)

tokens = lexer.getTokens()

print(tokens)

our_parser = my_parser.build_parser()
our_parser.parse(data, lexer.lexer)
