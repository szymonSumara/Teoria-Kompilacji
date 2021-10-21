import sys
from lexer import Lexer



args = sys.argv[1:]

if not args:
    print('\033[91m' + '[ERROR] : No file path provided')
    exit(1)


try:
    data = open(args[0], "r").read()
except FileNotFoundError:
    print('\033[91m' + '[ERROR] : File "' + args[0] + '" found')
    exit()



lexer =  Lexer()
lexer.tokenize(data)

for token in lexer.getTokens():
    print(token)
