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
            self.instructions.printTree()



    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("| " * indent + "For")
        print("| " * (indent + 1) +  str(self.id))
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


