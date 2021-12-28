from SymbolTable import *


type_table = {}

type_table['+'] = {}

type_table['+']['int'] = {}
type_table['+']['float'] = {}

type_table['+']['int']['int'] = 'int'
type_table['+']['int']['float'] = 'float'
type_table['+']['float']['int'] = 'float'
type_table['+']['float']['float'] = 'float'

#TODO to ^ jakub


def get_new_symbol(op, left, right):
    if type(left) != type(right):
        return None

    if isinstance(left, VectorSymbol):
        if op == '+' or op == '-':
            if left.size == right.size:
                new_type = check_type(op, left.type, right.type)
                if new_type:
                    return VectorSymbol('xd?', new_type, left.size)
        return None         # TODO dodać klase error Jakub

    if isinstance(left, MatrixSymbol): # TODO macierz Jakub
        return None

    if isinstance(left, VariableSymbol):
        new_type = check_type(op, left.type, right.type)
        if new_type:
            return VariableSymbol('xd?', new_type)
        return None


def check_type(op, left, right):
    try:
        return type_table[op][left][right]
    except KeyError:
        return None


if __name__ == '__main__':
    print(check_type('+', VectorSymbol('why', 'float', 10), VectorSymbol('not', 'int', 10)))
    print(check_type('-', 'float', 'int'))
