A = [[4 ,5]];
B = [[3, 2]];

C = A .+ B;

D = [6, 7];
E = [5, 2];

F = D + E;

if (5 < 7){
    print "idk";
}

if (A == B){
    print "what";
} else {
    print "ok";
}

a = 0;
b = 1;
while (b < 1000) {
    print b;
    print a;
    b += a;
    print b;
    a = b - a;
}

A = eye(3);
B = ones(3);
C = A .+ B;
print C;

D = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]];
D[0, 0] = 42;
#D[1:3, 2:4] = 7;
print D;
print D[2, 2];