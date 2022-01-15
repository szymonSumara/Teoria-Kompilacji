
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
            "+": self.add,
            "-": self.sub,
            "<": self.g,
            ">": self.l
        }

    def calculate(self, left_side, operator, right_side):
        return self.operators[operator](left_side, right_side)

    def add(self, left_side, right_side):
        return left_side + right_side

    def sub(self, left_side, right_side):
        return left_side - right_side

    def g(self, left_side, right_side):
        return left_side < right_side

    def l(self, left_side, right_side):
        return left_side > right_side

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

        self.memory.push(None)
        self.memory.insert(id, ne1)
        while self.memory.get(id) < ne2:
            try:
                self.memory.push(None)
                node.instruction.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break
            finally:
                self.memory.set(id, self.memory.get(id) + 1)
                self.memory.pop()
        self.memory.pop()

    @when(AST.While)
    def visit(self, node):


        while node.expression.accept(self):
            try:
                self.memory.push(None)
                node.instruction.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break
            finally:
                self.memory.pop()
       # node.instruction.accept(self)

    @when(AST.Block)
    def visit(self, node):
        self.memory.push(None)
        node.body.accept(self)
        self.memory.pop()

    @when(AST.Assignment)
    def visit(self, node):
        val = node.value.accept(self)
        self.memory.set(node.left_side.name, node.value.accept(self))


    @when(AST.Integer)
    def visit(self, node):
        return node.value

    @when(AST.Float)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.Vector)
    def visit(self, node):
        body = []
        for coordinate in node.body:
            body.append(coordinate.accept(self))
        return body

    @when(AST.Matrix)
    def visit(self, node):
        body = []
        for row in node.body:
            body.append(row.accept(self))
        return body

        return node.body

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(node.instruction.accept(self))


    @when(AST.Print)
    def visit(self, node):
        visitedValues  = []
        for arg in node.body:
            visitedValues.append(arg.accept(self))
        print(*visitedValues, sep=', ')

    @when(AST.Id)
    def visit(self, node):
        return self.memory.get(node.name)

    @when(AST.If)
    def visit(self, node):
        expression = node.expression.accept(self)
        print(expression)
        if expression:
            self.memory.push(None)
            node.instruction1.accept(self)
            self.memory.pop()
        elif node.instruction2 is not None:
            self.memory.push(None)
            node.instruction2.accept(self)
            self.memory.pop()



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


