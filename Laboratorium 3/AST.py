

class Node(object):
    pass

class Instructions(Node):
    def __init__(self, instruction, instructions=None):
        self.instruction = instruction
        self.instructions = instructions

class FlowKeyword(Node):
    def __init__(self, value):
        self.value = value

class For(Node):
    """for : FOR ID ASSIGN numeric_expression RANGE numeric_expression instruction"""
    def __init__(self, id, e1, e2, instructions):
        self.id = id
        self.e1 = e1
        self.e2 = e2
        self.instructions = instructions


class Print(Node):
    def __init__(self, body):
        self.body = body

class String(Node):
    def __init__(self, value):
        self.value = value;
# class IntNum(Node):
#     def __init__(self, value):
#         self.value = value
#
# class FloatNum(Node):
#     def __init__(self, value):
#         self.value = value
#
#
# class Variable(Node):
#     def __init__(self, name):
#         self.name = name
#
#
# class BinExpr(Node):
#     def __init__(self, op, left, right):
#         self.op = op
#         self.left = left
#         self.right = right


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
      
