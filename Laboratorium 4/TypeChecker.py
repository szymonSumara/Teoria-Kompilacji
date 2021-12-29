import AST
import SymbolTable

from type_table import *

# TODO scope - block Szymon
# TODO range Szymon

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        print(method)
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
        self.symbol_table = SymbolTable(None, 'god why')

    def visit_Expression(self, node):

        print('visit Expression')
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        symbol1 = self.visit(node.left_side)     # type1 = node.left.accept(self)
        symbol2 = self.visit(node.right_side)    # type2 = node.right.accept(self)
        op    = node.operator

        result_symbol = get_new_symbol(op, symbol1, symbol2)
        if isinstance(result_symbol, str):
            print("Error: {} in line {}".format(result_symbol, 'x'))
        return result_symbol


    def visit_Assignment(self, node):

        print(node.value)

        ex_symbol = self.visit(node.value)

        print('tu cos powinno byc ' , node.assignment)

        if node.assignment == '=':
            self.symbol_table.put(node.left_side.name, ex_symbol)


    def visit_Integer(self, node):
        print('visit Integer')
        return VariableSymbol('why does this exist', 'int')

    def visit_Float(self, node):
        return VariableSymbol('why does this exist', 'float')

    def visit_Vector(self, node):
        types = []
        for val in node.body:
            if not isinstance(val, VariableSymbol):
                print('Conflicting types in vector in line {}'.format('x'))
                return None
            types.append(self.visit(val).type)
        # TODO funkcja dajacy typ wektora Jakub
        return VectorSymbol('whyyyyyyy', 'int', len(node.body))


    def visit_Matrix(self, node):
        symbols = []
        for val in node.body:
            symbols.append(self.visit(val))
        # TODO funkcja dajacy typ wektora Jakub
        return VectorSymbol('whyyyyyyy', 'int', len(node.body))


    # TODO visit matrix rozmiar, typ Jakub

    def visit_Id(self, node):
        print('visit Id')
        tmp = self.symbol_table.get(node.name)
        if tmp is None:
            print("super error")
        return tmp






