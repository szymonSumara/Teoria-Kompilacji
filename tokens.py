
#+ operatory binare: +, -, *, /
#+ macierzowe operatory binarne (dla operacji element po elemencie): .+, .-, .*, ./
#+ operatory przypisania: =, +=, -=, *=, /=
#+ operatory relacyjne: <, >, <=, >=, !=, ==
#+ nawiasy: (,), [,], {,}
#+ operator zakresu: :
#+ transpozycja macierzy: '
#+ przecinek i średnik: , ;
#+ identyfikatory (pierwszy znak identyfikatora to litera lub znak _, w kolejnych znakach mogą dodatkowo wystąpić cyfry)
#+ liczby całkowite
#+ liczby zmiennoprzecinkowe
# stringi

from reserved import *

tokens = [
    # operatory binare: +, -, *, /
            'ADD',
            'SUB',
            'MUL',
            'DIV',
    # macierzowe operatory binarne (dla operacji element po elemencie): .+, .-, .*, ./
            'DOTADD',
            'DOTSUB',
            'DOTMUL',
            'DOTDIV',
    # operatory przypisania: =, +=, -=, *=, /=
            'ASSIGN',
            'SUBASSIGN',
            'MULASSIGN',
            'ADDASSIGN',
            'DIVASSIGN',
    # operatory relacyjne: <, >, <=, >=, !=, ==    
            'G',
            'L',
            'GE',
            'LE',
            'EQ',
            'NEQ',
    # nawiasy: (,), [,], {,}
            'ROUNDBRACKETSOPEN',
            'ROUNDBRACKETSCLOSE',
            'SQUAREBRACKETSOPEN',
            'SQUAREBRACKETSCLOSE',
            'CURLYBRACKETSOPEN',
            'CURLYBRACKETSCLOSE',
    # operator zakresu: :
            'RANGE',
    # transpozycja macierzy: '
            'TRANSPOSITION',
    # przecinek i średnik: , ;
            'COMMA',
            'SEMICOLON',
    # identyfikatory (pierwszy znak identyfikatora to litera lub znak _, w kolejnych znakach mogą dodatkowo wystąpić cyfry)      
            'ID',
    # liczby całkowite
            'INTNUM',
    # liczby zmiennoprzecinkowe      
            'FLOATNUM',       
    # stringi
            'STRING',
         ] + list(reserved.values())


# operatory binare: +, -, *, /
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
# macierzowe operatory binarne (dla operacji element po elemencie): .+, .-, .*, ./
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTDIV = r'\./'
t_DOTMUL = r'\.\*'
# operatory przypisania: =, +=, -=, *=, /=
t_ASSIGN = r'\='
t_SUBASSIGN = r'\-\='
t_MULASSIGN = r'\*\='
t_ADDASSIGN = r'\+\='
t_DIVASSIGN = r'\/\='
# operatory relacyjne: <, >, <=, >=, !=, == 
t_G = r'\<'
t_L = r'\>'
t_GE = r'\<\='
t_LE = r'\>\='
t_EQ = r'\=\='
t_NEQ = r'\!\='
# nawiasy: (,), [,], {,}
t_ROUNDBRACKETSOPEN = r'\('
t_ROUNDBRACKETSCLOSE = r'\)'
t_SQUAREBRACKETSOPEN = r'\['
t_SQUAREBRACKETSCLOSE = r'\]'
t_CURLYBRACKETSOPEN = r'\{'
t_CURLYBRACKETSCLOSE = r'\}'
# operator zakresu: :
t_RANGE = r'\:' 
# transpozycja macierzy ': 
t_TRANSPOSITION = r'\''  
# przecinek i średnik: ,  ;
t_COMMA = r'\,' 
t_SEMICOLON = r'\;'

# identyfikatory (pierwszy znak identyfikatora to litera lub znak _, w kolejnych znakach mogą dodatkowo wystąpić cyfry)     
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

#liczby zmiennoprzecinkowe
def t_FLOATNUM(t):
    r'(-)?\d+\.\d+'
    t.value = float(t.value)
    return t

# liczby całkowite
def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t
# stringi
def t_STRING(t):
    r'".*"'
    t.value = t.value[1:len(t.value) - 2]
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

 