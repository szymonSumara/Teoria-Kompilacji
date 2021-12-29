from SymbolTable import *

type_table = {}

type_table['+'] = {}

type_table['+']['int'] = {}
type_table['+']['float'] = {}
type_table['+']['string'] = {}

type_table['-']['int'] = {}
type_table['-']['float'] = {}

type_table['*']['int'] = {}
type_table['*']['float'] = {}

type_table['/']['int'] = {}
type_table['/']['float'] = {}

type_table['<']['int'] = {}
type_table['<']['float'] = {}

type_table['>']['int'] = {}
type_table['>']['float'] = {}

type_table['<=']['int'] = {}
type_table['<=']['float'] = {}

type_table['>=']['int'] = {}
type_table['>=']['float'] = {}

type_table['==']['int'] = {}
type_table['==']['float'] = {}
type_table['==']['string'] = {}
type_table['==']['bool'] = {}

type_table['!=']['int'] = {}
type_table['!=']['float'] = {}
type_table['!=']['string'] = {}
type_table['!=']['bool'] = {}

type_table['+']['int']['int'] = 'int'
type_table['+']['int']['float'] = 'float'
type_table['+']['float']['int'] = 'float'
type_table['+']['float']['float'] = 'float'
type_table['+']['string']['string'] = 'string'

type_table['-']['int']['int'] = 'int'
type_table['-']['int']['float'] = 'float'
type_table['-']['float']['int'] = 'float'
type_table['-']['float']['float'] = 'float'

type_table['*']['int']['int'] = 'int'
type_table['*']['int']['float'] = 'float'
type_table['*']['float']['int'] = 'float'
type_table['*']['float']['float'] = 'float'

type_table['/']['int']['int'] = 'float'
type_table['/']['int']['float'] = 'float'
type_table['/']['float']['int'] = 'float'
type_table['/']['float']['float'] = 'float'

type_table['>']['int']['int'] = 'bool'
type_table['>']['int']['float'] = 'bool'
type_table['>']['float']['int'] = 'bool'
type_table['>']['float']['float'] = 'bool'

type_table['<']['int']['int'] = 'bool'
type_table['<']['int']['float'] = 'bool'
type_table['<']['float']['int'] = 'bool'
type_table['<']['float']['float'] = 'bool'

type_table['>=']['int']['int'] = 'bool'
type_table['>=']['int']['float'] = 'bool'
type_table['>=']['float']['int'] = 'bool'
type_table['>=']['float']['float'] = 'bool'

type_table['<=']['int']['int'] = 'bool'
type_table['<=']['int']['float'] = 'bool'
type_table['<=']['float']['int'] = 'bool'
type_table['<=']['float']['float'] = 'bool'

type_table['==']['int']['int'] = 'bool'
type_table['==']['int']['float'] = 'bool'
type_table['==']['float']['int'] = 'bool'
type_table['==']['float']['float'] = 'bool'
type_table['==']['string']['string'] = 'bool'
type_table['==']['bool']['bool'] = 'bool'

type_table['!=']['int']['int'] = 'bool'
type_table['!=']['int']['float'] = 'bool'
type_table['!=']['float']['int'] = 'bool'
type_table['!=']['float']['float'] = 'bool'
type_table['!=']['bool']['bool'] = 'bool'


# TODO to ^ jakub


def get_new_symbol(op, left, right):
    if isinstance(left, VectorSymbol):
        if op == '+' or op == '-':
            if type(left) != type(right):
                return 'Can\'t {} Vector to {}'.format(op, type(right))
            if left.size != right.size:
                return 'Can\'t {} Vectors with sizes {} and {}'.format(op, left.size, right.size)
            new_type = check_type(op, left.type, right.type)
            if new_type:
                return VectorSymbol('xd?', new_type, left.size)
            return 'Can\'t {} Vector of type {} to Vector of type {}'.format(op, left.type, right.type)

        if op == '*.' or op == '/.' or op == '+.' or op == '-.':
            if isinstance(right, VariableSymbol):
                new_type = check_type(op[0], left.type, right.type)
                if new_type:
                    return VectorSymbol('xd?', new_type, left.size)
                return 'Can\'t {} Vector of type {} with Variable of type {}'.format(op, left.type, right.type)
            return 'Can\'t {} Vector to {}'.format(op, type(right))

        return 'Can\'t {} Vector to {}'.format(op, type(right))

    if isinstance(left, MatrixSymbol):
        if op == '+' or op == '-':
            if type(left) != type(right):
                return 'Can\'t {} Matrix to {}'.format(op, type(right))
            if left.size != right.size:
                return 'Can\'t {} Matrices with sizes {} and {}'.format(op, left.size, right.size)
            new_type = check_type(op, left.type, right.type)
            if new_type:
                return MatrixSymbol('xd?', new_type, left.size)
            return 'Can\'t {} Matrix of type {} to Matrix of type {}'.format(op, left.type, right.type)

        if op == '*.' or op == '/.' or op == '+.' or op == '-.':
            if isinstance(right, VariableSymbol):
                new_type = check_type(op[0], left.type, right.type)
                if new_type:
                    return MatrixSymbol('xd?', new_type, left.size)
                return 'Can\'t {} Matrix of type {} with Variable of type {}'.format(op, left.type, right.type)
            if isinstance(right, MatrixSymbol):
                if left.size != right.size:
                    return 'Can\'t {} Matrices with sizes {} and {}'.format(op, left.size, right.size)
                new_type = check_type(op[0], left.type, right.type)
                if new_type:
                    return MatrixSymbol('xd?', new_type, left.size)
                return 'Can\'t {} Matrix of type {} with Matrix of type {}'.format(op, left.type, right.type)
            return 'Can\'t {} Matrix with {}'.format(op, type(right))

        if op == '*':
            if type(left) != type(right):
                return 'Can\'t {} Matrix with {}'.format(op, type(right))
            if left.size[1] != right.size[0]:
                return 'Can\'t {} Matrices with sizes {} and {}'.format(op, left.size, right.size)
            new_type = check_type(op, left.type, right.type)
            if new_type:
                return MatrixSymbol('xd?', new_type, (left.size[0], right.size[1]))
            return 'Can\'t {} Matrix of type {} with Matrix of type {}'.format(op, left.type, right.type)

    if isinstance(left, VariableSymbol):
        if isinstance(right, VariableSymbol):
            new_type = check_type(op, left.type, right.type)
            if new_type:
                return VariableSymbol('xd?', new_type)
            return 'Can\'t {} Variable of type {} with Variable of type {}'.format(op, left.type, right.type)
        if op == '*.' or op == '/.' or op == '+.' or op == '-.':
            if isinstance(right, VectorSymbol):
                new_type = check_type(op, left.type, right.type)
                if new_type:
                    return VectorSymbol('xd?', new_type, right.size)
                return 'Can\'t {} Variable of type {} with Vector of type {}'.format(op, left.type, right.type)
            if isinstance(right, MatrixSymbol):
                new_type = check_type(op, left.type, right.type)
                if new_type:
                    return MatrixSymbol('xd?', new_type, right.size)
                return 'Can\'t {} Variable of type {} with Matrix of type {}'.format(op, left.type, right.type)
            return 'Unknown error, shouldn\'t happen'
        return 'Can\'t {} Variable with {}'.format(op, type(right))

    return 'Unknown error, shouldn\'t happen'


def vector_type(types):
    is_string = False
    is_float = False


def check_type(op, left, right):
    try:
        return type_table[op][left][right]
    except KeyError:
        return None


if __name__ == '__main__':
    print(check_type('+', VectorSymbol('why', 'float', 10), VectorSymbol('not', 'int', 10)))
    print(check_type('-', 'float', 'int'))
