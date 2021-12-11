
class Node(object):
    pass


class Function(Node):
    def __init__(self, fun_name, fun_body):
        self.fun_name = fun_name
        self.fun_body = fun_body


class FunctionBody(Node):
    def __init__(self, argument, next_argument=None):
        print(argument)
        self.argument = argument
        self.next_argument = next_argument


class Instructions(Node):
    def __init__(self, instruction, instructions=None):
        self.instruction = instruction
        self.instructions = instructions


class FlowKeyword(Node):
    def __init__(self, value):
        self.value = value


class For(Node):
    def __init__(self, id, e1, e2, instructions):
        self.id = id
        self.e1 = e1
        self.e2 = e2
        self.instructions = instructions


class Assignment(Node):
    def __init__(self, left_side, assignment, value):
        self.left_side = left_side
        self.assignment = assignment
        self.value = value


class Expression(Node):
    def __init__(self, left_side, operator, right_side):
        self.left_side = left_side
        self.operator = operator
        self.right_side = right_side


class Print(Node):
    def __init__(self, body):
        self.body = body

class String(Node):
    def __init__(self, value):
        self.value = value

class Integer(Node):
    def __init__(self, value):
        self.value = value


class Id(Node):
    def __init__(self, value):
        self.value = value


class Float(Node):
    def __init__(self, value):
        self.value = value


class Matrix(Node):
    def __init__(self, body=None):
        self.body = body


class MatrixBody(Node):
    def __init__(self, row, next_row=None):
        self.row = row
        self.next_row = next_row


class Range(Node):
    def __init__(self, var, fun_body):
        self.var = var
        self.fun_body = fun_body


class Vector(Node):
    def __init__(self, body=None):
        self.body = body


class VectorBody(Node):
    def __init__(self, item, next_item=None):
        self.item = item
        self.next_item = next_item

# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
