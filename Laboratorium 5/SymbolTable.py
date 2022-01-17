#!/usr/bin/python


class Symbol(object):
    pass


class VariableSymbol(Symbol): # (Symbol)

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.type_name = 'Variable'
    #


class VectorSymbol(Symbol): # (Symbol)

    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        self.type_name = 'Vector'


class MatrixSymbol(Symbol): # (Symbol)

    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        self.type_name = 'Matrix'


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.dict = {}
    #

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry

        actual = self
        while actual is not None:
            if name in actual.dict.keys():
                actual.dict[name] = symbol
                return
            actual = actual.parent

        self.dict[name] = symbol
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        if name in self.dict:
            return self.dict[name];
        else:
            if self.parent:
                return self.parent.get(name)

        return None
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


