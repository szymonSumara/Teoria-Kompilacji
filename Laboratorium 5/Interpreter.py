
import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)

class OperationManager:
    def __init__(self):
        self.operators = {
            "+" : self.add
        }

    def calculate(self, left_side, operator, right_side):
        return self.operators[operator](left_side, right_side)

    def add(self, left_side, right_side):
        return left_side + right_side


class Interpreter(object):


    def __init__(self):
        self.memory = MemoryStack()
        self.operationManager = OperationManager()

    @on('node')
    def visit(self, node):
        pass

    # @when(AST.BinOp)
    # def visit(self, node):
    #     r1 = node.left.accept(self)
    #     r2 = node.right.accept(self)
    #     # try sth smarter than:
    #     # if(node.op=='+') return r1+r2
    #     # elsif(node.op=='-') ...
    #     # but do not use python eval

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Expression)
    def visit(self, node):
        left_side = node.left_side.accept(self)
        right_side = node.right_side.accept(self)
        operator = node.operator
        return self.operationManager.calculate(left_side, operator, right_side)

    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.children:
            instruction.accept(self)

    @when(AST.For)
    def visit(self, node):
        id = node.id
        ne1 = node.ne1.accept(self)
        ne2 = node.ne2.accept(self)
        j = ne1
        while j < ne2:
            try:
                node.instruction.accept(self)
                j += 1
            except ContinueException:
                j += 1
                continue
            except BreakException:
                break


       # node.instruction.accept(self)

    @when(AST.Block)
    def visit(self, node):
        node.body.accept(self)

    @when(AST.Assignment)
    def visit(self, node):
        val = node.value.accept(self)
        self.memory.set(node.left_side.name, node.value.accept(self))



    @when(AST.Integer)
    def visit(self, node):
        return node.value


    @when(AST.Print)
    def visit(self, node):
        visitedValues  = []
        for arg in node.body:
            visitedValues.append(arg.accept(self))
        print(*visitedValues, sep=', ')

    @when(AST.Id)
    def visit(self, node):
        return self.memory.get(node.name)




    # @when(AST.Assignment)
    # def visit(self, node):
    #     pass

    # simplistic while loop interpretation
    # @when(AST.WhileInstr)
    # def visit(self, node):
    #     r = None
    #     while node.cond.accept(self):
    #         r = node.body.accept(self)
    #     return r


