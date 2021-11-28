
import ply.lex as lex
from tokens import * 



class Lexer:
    def __init__(self):
        self.tokens = []
        self.lexer = lex.lex()

    def tokenize(self, data):
        self.lexer.input(data)
        self.tokens = []
        token = self.lexer.token()
        
        while token :
            #token = self.tokenToStr(token)
            self.tokens.append(token)
            token = self.lexer.token()

    def tokenToStr(self,token):
        return str(token.lineno)+ " " + str(token.type) + "(" +str(token.value) + ")" 

    def getTokens(self):
        return self.tokens[:]
