import sys
from lexer import Lexer
import my_parser
from TreePrinter import TreePrinter
#
# args = sys.argv[1:]
#
# if not args:
#     print('\033[91m' + '[ERROR] : No file path provided')
#     exit(1)
#
#
# try:
#     data = open(args[0], "r").read()
# except FileNotFoundError:
#     print('\033[91m' + '[ERROR] : File "' + args[0] + '" found')
#     exit()


data = """
# control flow instruction

N = 10;
M = 20;

if(N==10)
    print "N==10";
else if(N!=10)
    print "N!=10";


if(N>5) {
    print "N>5";
}
else if(N>=0) {
    print "N>=0";
}

if(N<10) {
    print "N<10";
}
else if(N<=15)
    print "N<=15";

k = 10;
while(k>0)
    k = k - 1;

while(k>0) {
    if(k<5)
        i = 1;
    else if(k<10)
        i = 2;   
    else
        i = 3;
    
    k = k - 1;
}


for i = 1:N
  for j = i:M
    print i, j;
 

for i = 1:N {
    if(i<=N/16)
        print i;
    else if(i<=N/8)
        break;
    else if(i<=N/4)
        continue;
    else if(i<=N/2)
        return 0;
}


{
  N = 100;
  M = 200;  
}


A[10]/=10.9;

"""

data2 = """
# assignment operators
# binary operators
# transposition

C = -A;     # assignemnt with unary expression
C = B' ;    # assignemnt with matrix transpose
C = A+B ;   # assignemnt with binary addition
C = A-B ;   # assignemnt with binary substraction
C = A*B ;   # assignemnt with binary multiplication
C = A/B ;   # assignemnt with binary division
C = A.+B ;  # add element-wise A to B
C = A.-B ;  # substract B from A 
C = A.*B ;  # multiply element-wise A with B
C = A./B ;  # divide element-wise A by B

C += B ;  # add B to C 
C -= B ;  # substract B from C 
C *= A ;  # multiply A with C
C /= A ;  # divide A by C
"""

data3 = """
# special functions, initializations

A = zeros(5);  # create 5x5 matrix filled with zeros
B = ones(7);   # create 7x7 matrix filled with ones
I = eye(10);   # create 10x10 matrix filled with ones on diagonal and zeros elsewhere

# initialize 3x3 matrix with specific values
E1 = [ [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9] ] ;

A[1,3] = 0 ;

x = 2;
y = 2.5;
"""

data5 = '''
for j = 1:10 
    print "j";
    
for k = 2:7 
    print "k";
'''

data6 = '''
# assignment operators
# binary operators
# transposition

D1 = A.+B' ; # add element-wise A with transpose of B
D2 -= A.-B' ; # substract element-wise A with transpose of B
D3 *= A.*B' ; # multiply element-wise A with transpose of B
D4 /= A./B' ; # divide element-wise A with transpose of B
'''

data6 = '''
# special functions, initializations

A = zeros(5,4,2,3.3);  # create 5x5 matrix filled with zeros
B = ones(7);   # create 7x7 matrix filled with ones
I = eye(10);   # create 10x10 matrix filled with ones on diagonal and zeros elsewhere

E1 = [ [ 1, 2, 3],
       [ 4, 5, 6],
       [ 7, 8, 9] ];


A[1,3] = 0 ;
'''


data7 = """
# assignment operators
# binary operators
# transposition

D1 = A.+B' ; # add element-wise A with transpose of B
D2 -= A.-B' ; # substract element-wise A with transpose of B
D3 *= A.*B' ; # multiply element-wise A with transpose of B
D4 /= A./B' ; # divide element-wise A with transpose of B
"""

data8 = """
# control flow instruction

N = 10;
M = 20;
for i = 1:N {
    for j = i:M {
        print i, j;
    }
}

while(k>0) {
    if(k<5)
        i = 1;
    else if(k<10)
        i = 2;   
    else
        i = 3;
    
    k = k - 1;
}
"""

lexer = Lexer()
lexer.tokenize(data5)

tokens = lexer.getTokens()

print(tokens)

our_parser = my_parser.build_parser()
ast = our_parser.parse(data8, lexer.lexer)
print(ast)
ast.printTree()
