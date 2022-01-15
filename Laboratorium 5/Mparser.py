#!/usr/bin/python
import AST
from scanner import Scanner
import ply.yacc as yacc
import TreePrinter

class Mparser(object):
    def __init__(self):
        self.scanner = Scanner()
        self.scanner.build()

    tokens = Scanner.tokens

    precedence = (
        ("nonassoc", 'IFX'),
        ('nonassoc', 'ELSE'),
        ('right', '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
        ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'NEQ', 'EQ'),
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('left', 'DOTADD', 'DOTSUB'),
        ('left', 'DOTMUL', 'DOTDIV'),
        ('right', 'U_NEG'),
        ('right', '\'')
    )

    def p_error(self,p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")


    def p_program(self,p):
        """program : instructions_opt"""

        p[0] = AST.Program(p[1])
        # p[0].printTree(0)

    def p_instructions_opt(self,p):
        """instructions_opt : instructions
                            | """

        if len(p)>1:
            p[0] = AST.Instructions_Opt(p[1])
        else:
            p[0]= AST.Instructions_Opt(None)

    def p_instructions(self,p):
        """instructions : instructions instruction
                        | instruction """

        if len(p) > 2:
            p[0] = AST.Instructions(p[1], p[2])
        else:
            p[0] = AST.Instructions(None, p[1])

    def p_instruction(self,p):
        """instruction : instruction2 ';'
                        | loop
                        | block
                        | if """
        p[0]=p[1]

    def p_instruction2(self,p):
        """instruction2 : assignment
                        | return
                        | print
                        | continue
                        | break"""

        p[0] = p[1]
    def p_block(self,p):
        """ block : '{' instructions '}' """
        p[0]=AST.Block(p[2])

    def p_loop(self,p):
        """loop : for
                | while"""
        p[0]=p[1]

    def p_expression(self,p): #
        """expression  : expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression
                      | expression DOTADD expression
                      | expression DOTSUB expression
                      | expression DOTMUL expression
                      | expression DOTDIV expression
                      | expression EQ expression
                      | expression NEQ expression
                      | expression LT expression
                      | expression GE expression
                      | expression LE expression
                      | expression GT expression
                      | array_range
                      | u_neg
                      | transpose
                      | ID
                      | const """
        if len(p)>3:
            p[0]=AST.Expression(p[1],p[2],p[3])
        else:
            if not (isinstance(p[1],AST.Const) or isinstance(p[1],AST.Array_range) or isinstance(p[1],AST.Transpose) or isinstance(p[1],AST.UNeg)):
                p[0]=AST.Id(p[1])
            else:
                p[0] = AST.Expression(p[1],None,None)

    def p_const(self,p): #
        """const : INTNUM
                 | FLOATNUM
                 | STRING"""
        p[0] = AST.Const(p[1])


    def p_assign_operator(self,p): #
        """ operator : '='
                    | ADDASSIGN
                    | SUBASSIGN
                    | MULASSIGN
                    | DIVASSIGN  """
        p[0] = p[1]

    def p_assignment(self,p):
        """assignment : type operator expression
                    | type '=' matrix
                    | type '=' vector_
                    | type '=' fun """


        #if isinstance(p[3],AST.Expression):
        p[0]=AST.Assignment(p[1],p[2],p[3])
        # elif isinstance(p[3],AST.Fun):
        #     p[0]=AST.Assignment(AST.Type(p[1]),p[2],AST.Fun(p[3]))
        # elif isinstance(p[3],AST.Matrix):
        #     p[0]=AST.Assignment(AST.Type(p[1]),p[2],AST.Matrix(p[3]))
        # else:
        #     p[0] = AST.Assignment(AST.Type(p[1]), p[2], AST.Vector(p[3]))


    def p_type(self,p):
        """ type : ID
                | array_range """

        if isinstance(p[1],AST.Array_range):
            p[0]=AST.Type(p[1])
        else:
            p[0]=AST.Id(p[1])

    def p_fun(self,p):
        """ fun : funMatrix '(' expression ')' """
        p[0] = AST.Fun(p[1],p[3])

    def p_matrixFun(self,p):
        """funMatrix : ONES
                    | EYE
                    | ZEROS """
        p[0]=AST.MatrixFun(p[1])

    def p_break(self,p):
        """break : BREAK """
        p[0]=AST.Break()
    def p_transpose(self,p):
        r"""transpose : expression '\''  """
        p[0]=AST.Transpose(p[1])

    def p_return(self,p):
        """return : RETURN expression
                | RETURN """
        if len(p)>2:
            p[0] = AST.Return(p[2])
        else:
            p[0]=p[1]
    def p_continue(self,p):
        """continue : CONTINUE """
        p[0]=AST.Continue()

    def p_if(self,p):
        """ if : IF '(' expression ')' instruction  %prec IFX
               | IF '(' expression ')' instruction ELSE instruction """
        if len(p) >6  and p[6].lower() == "else":
            p[0]=AST.Choice(AST.If(p[3],p[5]),AST.Else(p[7]))
        else:
            p[0]=AST.Choice(AST.If(p[3], p[5]), None)

    def p_while(self,p):
        """while : WHILE '(' expression ')' instruction """
        p[0] = AST.While(p[3],p[5])

    def p_for(self,p):
        """for : FOR ID '=' expression ':' expression instruction"""
        p[0] = AST.For(p[2],p[4],p[6],p[7])

    def p_print(self,p):
        """print : PRINT print_helper """
        p[0]=AST.Print(p[2])

    def p_print_helper(self,p):
        """print_helper : expression
                        | print_helper ',' expression """
        if len(p)>2:
            p[0]=AST.Print_Helper(p[3],p[1])
        else:
            p[0]=AST.Print_Helper(p[1],None)

    def p_neg(self,p):
        """u_neg : '-' expression %prec U_NEG """
        p[0] = AST.UNeg(p[2])




    def p_matrix(self,p):
        """matrix : '[' matrix_body ']' """
        p[0]= AST.Matrix(p[2])


    def p_matrix_body(self,p):
        """matrix_body : vector_
                       | vector_ ',' matrix_body  """
        if len(p) > 2:
            p[0] = AST.Matrix_Body(p[1],p[3])
        else:
            p[0]=AST.Matrix_Body(p[1],None)

    def p_vector_(self,p):
        """vector_ : '[' vector_body ']'
                  | '[' ']'"""
        if len(p)>3 and p[2]!= None:
            p[0] = AST.Vector(p[2])
        else:
            p[0] = AST.Vector(None)


    def p_vector_body(self,p):
        """vector_body : vector_body ',' expression
                       | expression """

        if len(p) > 2:
            p[0] = AST.Vector_Body(p[1],p[3])
        else:
            p[0] = AST.Vector_Body(p[1],None)
    def p_array_range(self,p):  #
        """array_range : ID '[' expression ',' expression ']'"""
        p[0]=AST.Array_range(p[1],p[3],p[5])


#parser = yacc.yacc()
