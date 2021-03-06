#!/usr/bin/python

import ply.yacc as yacc

from tokens import tokens


def build_parser():
    precedence = (
        # to fill ...
        ("nonassoc", 'IFX'),
        ('nonassoc', 'ELSE'),
        # ('right', 'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
        ('nonassoc', 'L', 'G', 'LE', 'GE', 'NEQ', 'EQ'),

        ("left", 'ADD', 'SUB'),
        ('left', 'DOTADD', 'DOTSUB'),
        ('left', 'MUL', 'DIV'),
        ('left', 'DOTMUL', 'DOTDIV'),
        ('right', 'UMINUS'),
        ('right', 'TRANSPOSITION'),
        # to fill ...
    )

    # tokens = self.tokens

    def p_instructions(p):
        """instructions : instruction
                        | instruction instructions"""

    def p_instruction(p):
        """instruction : block
                       | conditional
                       | loop
                       | statement SEMICOLON
                       | error SEMICOLON"""

    def p_statement(p):
        """statement : assignment
                     | flow_keyword
                     | fun
                     | return
                     | print"""

    def p_flow_keyword(p):
        """flow_keyword : BREAK
                        | CONTINUE"""

    def p_block(p):
        """block : CURLYOPEN instructions CURLYCLOSE
                 | CURLYOPEN error CURLYCLOSE"""

    def p_print(p):
        """print : PRINT print_body"""

    def p_print_body(p):
        """print_body : string
                      | expression
                      | string COMMA print_body
                      | expression COMMA print_body"""

    def p_return(p):
        """return : RETURN expression
                | RETURN"""

    def p_string(p):
        """string : STRING"""

    def p_conditional(p):
        """conditional : IF ROUNDOPEN expression ROUNDCLOSE instruction %prec IFX
                       | IF ROUNDOPEN expression ROUNDCLOSE instruction ELSE instruction"""

    def p_loop(p):
        """loop : while
                | for"""

    def p_while(p):
        """while : WHILE ROUNDOPEN expression ROUNDCLOSE instruction"""

    def p_for(p):
        """for : FOR ID ASSIGN numeric_expression RANGE numeric_expression instruction"""

    def p_fun(p):
        """fun : fun_name ROUNDOPEN fun_args ROUNDCLOSE
               | fun_name ROUNDOPEN error ROUNDCLOSE"""

    def p_fun_args(p):
        """fun_args : numeric_expression
                    | numeric_expression COMMA fun_args"""

    def p_fun_name(p):
        """fun_name : ZEROS
                    | ONES
                    | EYE"""

    def p_assignment(p):
        """assignment : assignment_left_side assignment_operator expression
                      | assignment_left_side ASSIGN string
                      | assignment_left_side ASSIGN matrix"""

    def p_assignment_left_side(p):
        """assignment_left_side : var"""

    def p_assignment_operator(p):
        """assignment_operator : ASSIGN
                               | ADDASSIGN
                               | SUBASSIGN
                               | MULASSIGN
                               | DIVASSIGN"""

    def p_matrix(p):
        """matrix : SQUAREOPEN matrix_body SQUARECLOSE
                  | SQUAREOPEN SQUARECLOSE"""

    def p_matrix_body(p):
        """matrix_body : vector
                       | matrix_body COMMA vector"""

    def p_vector(p):
        """vector : SQUAREOPEN vector_body SQUARECLOSE
                  | SQUAREOPEN SQUARECLOSE"""

    def p_vector_body(p):
        """vector_body : numeric_expression
                       | vector_body COMMA numeric_expression"""

    def p_expression(p):
        """expression : comparison_expression
                    | numeric_expression
                    | fun
                    """

    def p_comparison_expression(p):
        """comparison_expression : numeric_expression L numeric_expression
               | numeric_expression G numeric_expression
               | numeric_expression EQ numeric_expression
               | numeric_expression NEQ numeric_expression
               | numeric_expression GE numeric_expression
               | numeric_expression LE numeric_expression
               | ROUNDOPEN comparison_expression ROUNDCLOSE"""

    def p_expression_plus(p):
        'numeric_expression : numeric_expression ADD term'

    def p_expression_minus(p):
        'numeric_expression : numeric_expression SUB term'

    def p_expression_dot(p):
        """numeric_expression : numeric_expression DOTADD term
                            | numeric_expression DOTSUB term"""

    def p_expression_term(p):
        'numeric_expression : term'

    def p_term_times(p):
        'term : term MUL factor'

    def p_term_div(p):
        'term : term DIV factor'

    def p_term_dot(p):
        """term : term DOTMUL factor
                | term DOTDIV factor"""

    def p_term_factor(p):
        """term : factor"""

    def p_factor_floatnum(p):
        'factor : FLOATNUM'

    def p_factor_intnum(p):
        'factor : INTNUM'

    def p_factor_var(p):
        """factor : var"""

    def p_factor_expr(p):
        """factor : ROUNDOPEN numeric_expression ROUNDCLOSE
                | unary_operator"""

    def p_unary_operator(p):
        """unary_operator : negation
                    | transposition"""

    def p_negation(p):
        """negation : SUB factor %prec UMINUS"""

    def p_transposition(p):
        r"""transposition : factor TRANSPOSITION"""

    def p_var(p):
        """var : ID
               | ID SQUAREOPEN fun_args SQUARECLOSE
               """

    # Error rule for syntax errors
    def p_error(p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")

    return yacc.yacc()

# to finish the grammar
# ....
