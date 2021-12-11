from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        self.instruction.printTree()
        if self.instructions:
            self.instructions.printTree(indent)


    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("| " * indent + self.assignment)
        self.left_side.printTree(indent + 1)
        self.value.printTree(indent=indent+1)


    @addToClass(AST.Function)
    def printTree(self, indent=0):
        print("| " * indent + self.fun_name)
        self.fun_body.printTree(indent=indent+1)


    @addToClass(AST.FunctionBody)
    def printTree(self, indent=0):
        self.argument.printTree(indent)
        if self.next_argument:
            self.next_argument.printTree(indent)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("| " * indent + "For")
        self.id.printTree(indent + 1)
        print("| " * (indent + 1) + "RANGE")
        print("| " * (indent + 2) + str(self.e1))
        print("| " * (indent + 2) + str(self.e2))
        self.instructions.printTree(indent=indent+1)
        # fill in the body

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print("| " * indent + "Print")
        self.body.printTree(indent=indent+1)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("| " * indent + self.value)

    @addToClass(AST.Id)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))


    @addToClass(AST.Integer)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))

    @addToClass(AST.Float)
    def printTree(self, indent=0):
        print("| " * indent + str(self.value))

    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        print("| " * indent + "Matrix")
        if self.body:
            self.body.printTree(indent + 1)

    @addToClass(AST.MatrixBody)
    def printTree(self, indent=0):
        self.row.printTree(indent)
        if self.next_row:
            self.next_row.printTree(indent)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("| " * indent + "Vector")
        if self.body:
            self.body.printTree(indent + 1)

    @addToClass(AST.VectorBody)
    def printTree(self, indent=0):
        self.item.printTree(indent)
        if self.next_item:
            self.next_item.printTree(indent)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print("| " * indent + "REF")
        self.var.printTree(indent +1 )
        self.fun_body.printTree(indent + 1 )


    @addToClass(AST.FlowKeyword)
    def printTree(self, indent=0):
        print("Flow")
        # fill in the body


    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass    
        # fill in the body


    # define printTree for other classes
    # ...


