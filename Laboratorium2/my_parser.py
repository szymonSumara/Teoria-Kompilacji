#!/usr/bin/python

import ply.yacc as yacc

from tokens import tokens


class Parser:
    def __init__(self):
        self.tokens = tokens

    def parse(self):
        precedence = (
            # to fill ...
            ("left", 'ADD', 'SUB'),
            # to fill ...
        )
        #tokens = self.tokens
        def p_expression_plus(p):
            'expression : expression ADD term'
            p[0] = p[1] + p[3]

        def p_expression_minus(p):
            'expression : expression SUB term'
            p[0] = p[1] - p[3]

        def p_expression_term(p):
            'expression : term'
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
            'factor : ROUNDBRACKETSOPEN expression ROUNDBRACKETSCLOSE'
            p[0] = p[2]

        # Error rule for syntax errors
        def p_error(p):
            print("Syntax error in input!")

        return yacc.yacc()






# to finish the grammar
# ....



