from __future__ import print_function
import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for ins in self.children:
            ins.printTree(indent)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("| " * indent + self.assignment)
        self.left_side.printTree(indent + 1)
        self.value.printTree(indent=indent + 1)

    @addToClass(AST.Function)
    def printTree(self, indent=0):
        print("| " * indent + self.fun_name)
        self.fun_body.printTree(indent=indent + 1)

    @addToClass(AST.FunctionBody)
    def printTree(self, indent=0):
        self.argument.printTree(indent)
        if self.next_argument:
            self.next_argument.printTree(indent)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("| " * indent + "FOR")
        print("| " * (indent + 1) + self.id)
        print("| " * (indent + 1) + "RANGE")
        self.ne1.printTree(indent=indent + 2)
        self.ne2.printTree(indent=indent + 2)
        self.instruction.printTree(indent=indent + 1)
        # fill in the body

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print("| " * indent + "WHILE")
        self.expression.printTree(indent=indent + 1)
        self.instruction.printTree(indent=indent + 1)
        # fill in the body

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print("| " * indent + "IF")
        self.expression.printTree(indent=indent + 1)
        print("| " * indent + "THEN")
      # print(self.instruction1)
        self.instruction1.printTree(indent=indent + 1)
        if self.instruction2:
            print("| " * indent + "ELSE")
            self.instruction2.printTree(indent=indent + 1)
        # fill in the body

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print("| " * indent + "PRINT")
        self.body.printTree(indent=indent + 1)

    @addToClass(AST.PrintBody)
    def printTree(self, indent=0):
        self.argument.printTree(indent)
        if self.next_argument:
            self.next_argument.printTree(indent)

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print("| " * indent + "RETURN")
        if self.instruction:
            self.instruction.printTree(indent=indent + 1)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("| " * indent + self.value)

    @addToClass(AST.Id)
    def printTree(self, indent=0):
        print("| " * indent + str(self.name))

    @addToClass(AST.Integer)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))

    @addToClass(AST.Float)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))

    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        print("| " * indent + "MATRIX")
        for val in self.body:
            val.printTree(indent + 1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("| " * indent + "VECTOR")
        for val in self.body:
            val.printTree(indent + 1)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print("| " * indent + "REF")
        self.var.printTree(indent + 1)
        self.fun_body.printTree(indent + 1)

    @addToClass(AST.FlowKeyword)
    def printTree(self, indent=0):
        print("| " * indent + self.value)
        # fill in the body

    @addToClass(AST.Expression)
    def printTree(self, indent=0):
        print("| " * indent + self.operator)
        self.left_side.printTree(indent + 1)
        self.right_side.printTree(indent=indent + 1)
        # fill in the body

    @addToClass(AST.UMinus)
    def printTree(self, indent=0):
        print("| " * indent + '-')
        self.factor.printTree(indent=indent + 1)

    @addToClass(AST.Transposition)
    def printTree(self, indent=0):
        print("| " * indent + 'TRANSPOSE')
        self.factor.printTree(indent=indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body

    # define printTree for other classes
    # ...
