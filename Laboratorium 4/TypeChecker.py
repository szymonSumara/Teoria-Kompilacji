import AST

import SymbolTable

from type_table import *

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):


    def __init__(self):
        self.symbol_table = SymbolTable.SymbolTable(None, 'god why')

    def visit_Expression(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        symbol1 = self.visit(node.left)     # type1 = node.left.accept(self)
        symbol2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op

        result_symbol = get_new_symbol(op, symbol1.type, symbol2.type)
        if result_symbol is None:
            print("Type error in line {}".format('x'))
        return result_symbol


    def visit_Assigment(self, node):

        ex_symbol = self.visit(node.value)

        if node.assignment == '=':
            self.symbol_table.put(node.left_side, ex_symbol)


    def visit_Integer(self, node):
        return VariableSymbol('why does this exist', 'int')

    def visit_Float(self, node):
        return VariableSymbol('why does this exist', 'float')
 

    def visit_Var(self, node):
        tmp = self.symbol_table.get(node.name)
        if tmp is None:
            print("super error")
        return tmp
        


