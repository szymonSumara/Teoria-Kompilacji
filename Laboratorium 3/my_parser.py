#!/usr/bin/python

import ply.yacc as yacc

from tokens import tokens
import AST

def build_parser():
    precedence = (
        # to fill ...
        ("nonassoc", 'IFX'),
        ('nonassoc', 'ELSE'),
        ('nonassoc', 'L', 'G', 'LE', 'GE', 'NEQ', 'EQ'),
        ('right', 'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
        ("left", 'ADD', 'SUB'),
        ('left', 'MUL', 'DIV'),
        ('left', 'DOTADD', 'DOTSUB'),
        ('left', 'DOTMUL', 'DOTDIV'),
        ('right', 'UMINUS'),
        ('right', 'TRANSPOSITION'),
        # to fill ...
    )

    # tokens = self.tokens

    def p_instructions(p):
        """instructions : instruction
                        | instruction instructions"""
        if(len(p) <= 2):
            p[0] = AST.Instructions(p[1])
        else:
            p[0] = AST.Instructions(p[1],p[2])

    def p_instruction(p):
        """instruction : block
                       | conditional
                       | loop
                       | statement SEMICOLON
                       | error SEMICOLON"""
        p[0] = p[1]

    def p_statement(p):
        """statement : assignment
                     | flow_keyword
                     | fun
                     | return
                     | print"""
        p[0] = p[1]

    def p_flow_keyword(p):
        """flow_keyword : BREAK
                        | CONTINUE"""
        p[0] = AST.FlowKeyword(p[1])

    def p_block(p):
        """block : CURLYOPEN instructions CURLYCLOSE
                 | CURLYOPEN error CURLYCLOSE"""
        p[0] = p[2]

    def p_print(p):
        """print : PRINT print_body"""
        p[0] = AST.Print(p[2])

    def p_print_body(p):
        """print_body : string
                      | expression
                     | string COMMA print_body
                     | expression COMMA print_body"""
        if len(p) == 2:
            p[0] = AST.PrintBody(p[1])
        else:
            p[0] = AST.PrintBody(p[1], p[3])


    def p_return(p):
        """return : RETURN expression
                | RETURN"""

    def p_string(p):
        """string : STRING"""
        p[0] = AST.String(p[1])

    def p_conditional(p):
        """conditional : IF ROUNDOPEN expression ROUNDCLOSE instruction %prec IFX
                       | IF ROUNDOPEN expression ROUNDCLOSE instruction ELSE instruction"""
        if len(p) == 6:
            p[0] = AST.If(p[3], p[5])
        else:
            p[0] = AST.If(p[3], p[5], p[7])

    def p_loop(p):
        """loop : while
                | for"""
        p[0] = p[1]

    def p_while(p):
        """while : WHILE ROUNDOPEN expression ROUNDCLOSE instruction"""
        p[0] = AST.While(p[3], p[5])

    def p_for(p):
        """for : FOR ID ASSIGN numeric_expression RANGE numeric_expression instruction"""
        p[0] = AST.For(p[2], p[4], p[6], p[7])

    def p_fun(p):
        """fun : fun_name ROUNDOPEN fun_body ROUNDCLOSE
               | fun_name ROUNDOPEN error ROUNDCLOSE"""
        p[0] = AST.Function(p[1], p[3])

    def p_fun_body(p):
        """fun_body : numeric_expression
                    | numeric_expression COMMA fun_body"""

        if(len(p) <= 2):
            p[0] = AST.FunctionBody(p[1])
        else:
            p[0] = AST.FunctionBody(p[1], p[3])


    def p_fun_name(p):
        """fun_name : ZEROS
                    | ONES
                    | EYE"""
        p[0] = p[1]

    def p_assignment(p):
        """assignment : assignment_left_side assignment_operator expression
                      | assignment_left_side ASSIGN string
                      | assignment_left_side ASSIGN matrix"""
        p[0] = AST.Assignment(p[1], p[2], p[3])



    def p_assignment_left_side(p):
        """assignment_left_side : var"""
        p[0] = p[1]

    def p_assignment_operator(p):
        """assignment_operator : ASSIGN
                               | ADDASSIGN
                               | SUBASSIGN
                               | MULASSIGN
                               | DIVASSIGN"""
        p[0] = p[1]

    def p_matrix(p):
        """matrix : SQUAREOPEN matrix_body SQUARECLOSE
                  | SQUAREOPEN SQUARECLOSE"""

        if len(p) <= 2:
            p[0] = AST.Matrix()
        else:
            p[0] = AST.Matrix(p[2])


    def p_matrix_body(p):
        """matrix_body : vector
                       | vector  COMMA matrix_body"""
        if len(p) <= 2:
            p[0] = AST.MatrixBody(p[1])
        else:
            p[0] = AST.MatrixBody(p[1], p[3])

    def p_vector(p):
        """vector : SQUAREOPEN vector_body SQUARECLOSE
                  | SQUAREOPEN SQUARECLOSE"""

        if len(p) < 3:
            p[0] = AST.Vector()
        else:
            p[0] = AST.Vector(p[2])

    def p_vector_body(p):
        """vector_body : numeric_expression
                       | numeric_expression COMMA  vector_body"""
        if len(p) <= 2:
            p[0] = AST.VectorBody(p[1])
        else:
            p[0] = AST.VectorBody(p[1], p[3])

    def p_expression(p):
        """expression : comparison_expression
                    | numeric_expression
                    | fun"""
        p[0] = p[1]

    def p_comparison_expression(p):
        """comparison_expression : numeric_expression L numeric_expression
               | numeric_expression G numeric_expression
               | numeric_expression EQ numeric_expression
               | numeric_expression NEQ numeric_expression
               | numeric_expression GE numeric_expression
               | numeric_expression LE numeric_expression
               | ROUNDOPEN comparison_expression ROUNDCLOSE"""
        p[0] = AST.Expression(p[1], p[2], p[3])





    def p_expression_plus(p):
        'numeric_expression : numeric_expression ADD term'
        p[0] = AST.Expression(p[1], p[2], p[3])


    def p_expression_minus(p):
        'numeric_expression : numeric_expression SUB term'
        p[0] = AST.Expression(p[1], p[2], p[3])


    def p_expression_dot(p):
        """numeric_expression : numeric_expression DOTADD term
                            | numeric_expression DOTSUB term"""
        p[0] = AST.Expression(p[1], p[2], p[3])

    def p_expression_term(p):
        'numeric_expression : term'
        p[0] = p[1]
        print(p[1])

    def p_term_times(p):
        'term : term MUL factor'
        p[0] = AST.Expression(p[1], p[2], p[3])

    def p_term_div(p):
        'term : term DIV factor'
        p[0] = AST.Expression(p[1], p[2], p[3])

    def p_term_dot(p):
        """term : term DOTMUL factor
                | term DOTDIV factor"""
        p[0] = AST.Expression(p[1], p[2], p[3])

    def p_term_factor(p):
        """term : factor"""
        p[0] = p[1]

    def p_factor_floatnum(p):
        'factor : FLOATNUM'
        p[0] = AST.Float(p[1])

    def p_factor_intnum(p):
        'factor : INTNUM'
        p[0] = AST.Integer(p[1])

    def p_factor_var(p):
        """factor : var"""
        p[0]= p[1]

    def p_factor_expr(p):
        """factor : ROUNDOPEN numeric_expression ROUNDCLOSE
                | unary_operator"""
        if len(p) == 3:
            p[0] = p[2]
        else:
            p[0] = p[1]

    def p_unary_operator(p):
        """unary_operator : negation
                    | transposition"""
        p[0] = p[1]

    def p_negation(p):
        """negation : SUB factor %prec UMINUS"""
        p[0] = AST.UMinus(p[2])

    def p_transposition(p):
        r"""transposition : factor TRANSPOSITION"""
        p[0] = AST.Transposition(p[1])

    def p_var(p):
        """var : ID
               | var SQUAREOPEN fun_body SQUARECLOSE
               """
        if len(p) <= 2:
            p[0] = AST.Id(p[1])
        else:
            p[0] = AST.Range(p[1], p[3])
    # Error rule for syntax errors
    def p_error(p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")

    return yacc.yacc()

# to finish the grammar
# ....
