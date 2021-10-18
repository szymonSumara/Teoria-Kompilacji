# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

reserved = {'break': 'BREAK',
            'continue': 'CONTINUE',
            'if': 'IF',
            'else': 'ELSE',
            }

# List of token names.   This is always required
tokens = [
             'ID',
             'INTNUM',
             'ADD',
             'SUB',
             'MUL',
             'DIV',
             'DOTADD',
             'DOTSUB',
             'DOTMUL',
             'DOTDIV',
             'ASSIGN',
             'SUBASSIGN',
             'MULASSIGN',
             'ADDASSIGN',
             'DIVASSIGN',
             'G',
             'L',
             'GE',
             'LE',
             'DIFFERENT',
             'EQUAL',
             'LPAREN',
             'RPAREN',
             'LSQBRACK',
             'RSQBRACK',
             'LBRACE',
             'RBRACE'
             'RANGE',
             'TRANSPOSITION',
             'COMMA',
             'SEMICOLON',
    'STRING',
         ] + list(reserved.values())

# Regular expression rules for simple tokens
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTDIV = r'\./'
t_DOTMUL = r'\.\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# A regular expression rule with some action code
def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'".*"'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3 + (4 * 10
  .+ -20 *2)) koko)
  if
  ifof
  "foka"
  "zab"a
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
