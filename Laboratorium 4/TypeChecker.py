import AST
import SymbolTable

from type_table import *

nested_loops_number = 0



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
            print("{} in line {}".format(result_symbol, node.line_number))
        return result_symbol


    def visit_Assignment(self, node):

        ex_symbol = self.visit(node.value)

        if node.assignment == '=':
            if isinstance(node.left_side, AST.Range):
                left_side_symbol = self.visit(node.left_side)
                if left_side_symbol:
                    left_side_type = left_side_symbol.type
                    if left_side_type != ex_symbol.type:
                        print("Assigment: Invalid types")
            else:
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
        for i in range(len(node.body)):
            val = node.body[i]
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
            node.body[i] = visited_val

        new_type = vector_type(types)
        if new_type:
            return MatrixSymbol('whyyyyyyy', new_type, (len(node.body), node.body[0].size))
        print('Conflicting types of Vectors in Matrix in line {}'.format('x'))
        return None

    def visit_Id(self, node):
        tmp = self.symbol_table.get(node.name)
        if tmp is None:
            print("Variable {} referenced before assignment in line {}".format(node.name, node.line_number))
        return tmp

    def visit_Block(self, node):
        print("Block")
        self.symbol_table = self.symbol_table.pushScope('new');
        self.visit(node.body)
        self.symbol_table = self.symbol_table.popScope();
        return None;

    def visit_Range(self, node):
        var = self.symbol_table.get(node.var.name)

        if var is None:
            return print("Variable undefined")
        if isinstance(var, MatrixSymbol):

            if len(node.fun_body.arguments) != 2:
                return print("Invalid arguments number")
            if not 0 <= node.fun_body.arguments[0].value < var.size[0] or not 0 <= node.fun_body.arguments[1].value < var.size[1]:
                return print("Out of range in line {0}.".format(node.line_number))
            return VariableSymbol("why this exist", var.type)
        if isinstance(var, VectorSymbol):
            if len(node.fun_body.arguments) != 1:
                return print("Invalid arguments number")
            if 0 > node.fun_body.arguments[0].value >= var.size :
                return print("Out of range")
            return VariableSymbol("why this exist", var.type)
        return print("Range unsupported type Range can be use only with Matrix and Vector")


    def visit_String(self,node):
        return VariableSymbol("something", "string");

    def visit_For(self, node):
        # TODO: co z range ?
        global nested_loops_number
        nested_loops_number += 1
        self.visit(node.instruction)
        nested_loops_number -= 1
    def visit_While(self,node):
        # TODO: co z binary expresion ?
        global nested_loops_number
        nested_loops_number += 1
        self.visit(node.instruction)
        nested_loops_number -= 1

    def visit_FlowKeyword(self, node):
        if nested_loops_number == 0:
            print(node.value + " outside loop")

    def visit_Function(self, node):
        size = node.fun_body.arguments[0].value;
        return MatrixSymbol("bla bla", "int", (size, size))

    def visit_Return(self, node):
        expresion_result = self.visit(node.instruction)
        if expresion_result == None:
            print("Return: undefinded value in line {}".format(node.line_number) )

    def visit_Print(self, node):
        for element in node.body:
            self.visit(element)


