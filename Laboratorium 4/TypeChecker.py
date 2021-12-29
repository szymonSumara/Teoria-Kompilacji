import AST
import SymbolTable

from type_table import *

# TODO scope - block Szymon
# TODO range Szymon

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
        self.symbol_table = SymbolTable(None, 'god why')

    def visit_Expression(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        symbol1 = self.visit(node.left_side)     # type1 = node.left.accept(self)
        symbol2 = self.visit(node.right_side)    # type2 = node.right.accept(self)
        op    = node.operator

        result_symbol = get_new_symbol(op, symbol1, symbol2)
        if isinstance(result_symbol, str):
            print("{} in line {}".format(result_symbol, 'x'))
            return None
        return result_symbol


    def visit_Assignment(self, node):
        ex_symbol = self.visit(node.value)

        if node.assignment == '=':
            if ex_symbol:
                self.symbol_table.put(node.left_side.name, ex_symbol)


    def visit_Integer(self, node):
        return VariableSymbol('why does this exist', 'int')

    def visit_Float(self, node):
        return VariableSymbol('why does this exist', 'float')

    def visit_Vector(self, node):
        types = []
        for val in node.body:
            visited_val = self.visit(val)
            if not isinstance(visited_val, VariableSymbol):
                print('Element of Vector is not a Variable in line {}'.format('x'))
                return None
            types.append(visited_val.type)
        new_type = vector_type(types)
        if new_type:
            return VectorSymbol('whyyyyyyy', new_type, len(node.body))
        print('Conflicting types in Vector in line {}'.format('x'))
        return None


    def visit_Matrix(self, node):
        types = []
        size = None
        for val in node.body:
            visited_val = self.visit(val)
            types.append(visited_val.type)
            if size:
                if size != visited_val.size:
                    print('Conflicting sizes of Vectors in Matrix in line {}'.format('x'))
                    return None
            else:
                size = visited_val.size
            if not isinstance(visited_val, VectorSymbol):
                print('Element of matrix is not a Vector in line {}'.format('x'))
                return None

        new_type = vector_type(types)
        if new_type:
            return MatrixSymbol('whyyyyyyy', new_type, (len(node.body), size))
        print('Conflicting types of Vectors in Matrix in line {}'.format('x'))
        return None

    def visit_Function(self, node):
        symbols = []
        for arg in node.fun_body:
            symbols.append(self.visit(arg))

        if node.fun_name == 'ones' or node.fun_name == 'zeros' or node.fun_name == 'eye':
            if len(symbols) > 2 or len(symbols) < 1:
                print('Bad number of arguments for function {} in line {}'.format(node.fun_name, 'x'))
                return None
            for sym in symbols:
                if sym.type != 'int':
                    print('Bad argument for function {} in line {}'.format(node.fun_name, 'x'))
                    return None
            if len(symbols) == 2:
                return MatrixSymbol('what', 'int', (node.fun_body[0].value, node.fun_body[1].value))
            return MatrixSymbol('what', 'int', (node.fun_body[0].value, node.fun_body[0].value))

        print('Function {} is not defined in line {}'.format(node.fun_name, 'x'))
        return None

    def visit_Id(self, node):
        tmp = self.symbol_table.get(node.name)
        if tmp is None:
            print("Variable {} referenced before assignment in line {}".format(node.name, 'x'))
        return tmp






