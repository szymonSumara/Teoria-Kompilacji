#!/usr/bin/python

import ply.yacc as yacc

from tokens import tokens


def build_parser():
    precedence = (
        # to fill ...
        ("nonassoc", 'IFX'),
        ('nonassoc', 'ELSE'),

        ("left", 'ADD', 'SUB'),
        ('left', 'MUL', 'DIV'),
        ('left', 'DOTADD', 'DOTSUB'),
        ('left', 'DOTMUL', 'DOTDIV'),
        ('right', 'TRANSPOSITION')
        # to fill ...
    )

    # tokens = self.tokens

    def p_instructions(p):
        """instructions : instruction
                        | instruction instructions"""

    def p_instruction(p):
        """instruction : block
                       | conditional
                       | statement SEMICOLON
                       | error SEMICOLON"""

    def p_statement(p):
        """statement : assignment
                     | flow_keyword
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

    def p_assignment(p):
        """assignment : assignment_left_side assignment_operator expression
                      | assignment_left_side ASSIGN string"""

    def p_assignment_left_side(p):
        """assignment_left_side : ID"""

    def p_assignment_operator(p):
        """assignment_operator : ASSIGN
                               | ADDASSIGN
                               | SUBASSIGN
                               | MULASSIGN
                               | DIVASSIGN"""

    def p_expression(p):
        """expression : comparison_expression
                    | numeric_expression"""

    def p_comparison_expression(p):
        """comparison_expression : numeric_expression L numeric_expression
               | numeric_expression G numeric_expression
               | numeric_expression EQ numeric_expression
               | numeric_expression NEQ numeric_expression
               | numeric_expression GE numeric_expression
               | numeric_expression LE numeric_expression
               | ROUNDOPEN comparison_expression ROUNDCLOSE"""

    def p_expression_id(p):
        """numeric_expression : ID"""

    def p_expression_plus(p):
        'numeric_expression : numeric_expression ADD term'
        p[0] = p[1] + p[3]

    def p_expression_minus(p):
        'numeric_expression : numeric_expression SUB term'
        p[0] = p[1] - p[3]

    def p_expression_term(p):
        'numeric_expression : term'
        p[0] = p[1]

    def p_term_times(p):
        'term : term MUL factor'
        p[0] = p[1] * p[3]

    def p_term_div(p):
        'term : term DIV factor'
        p[0] = p[1] / p[3]

    def p_term_factor(p):
        'term : factor'
        p[0] = p[1]

    def p_factor_floatnum(p):
        'factor : FLOATNUM'
        p[0] = p[1]

    def p_factor_intnum(p):
        'factor : INTNUM'
        p[0] = p[1]

    def p_factor_expr(p):
        'factor : ROUNDOPEN numeric_expression ROUNDCLOSE'
        p[0] = p[2]

    # Error rule for syntax errors
    def p_error(p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")

    return yacc.yacc()

# to finish the grammar
# ....
