#!/usr/bin/python


class Symbol(object):
    pass


class VariableSymbol(Symbol): # (Symbol)

    def __init__(self, name, type):
        self.name = name
        self.type = type
    #


class VectorSymbol(Symbol): # (Symbol)

    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size


class MatrixSymbol(Symbol): # (Symbol)

    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.dict = {}
    #

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.dict[name] = symbol
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        tmp = self.dict[name]
        if tmp is None:
            if self.parent:
                return self.parent.get(name)
        return tmp
    #

    def getParentScope(self):
        return self.parent
    #

    def pushScope(self, name):
        return SymbolTable(self, 'xd?')
    #

    def popScope(self):
        return self.parent
    #


