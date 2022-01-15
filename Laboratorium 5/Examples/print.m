a = 0;
b = 1;
c = [1, 2, 3];
d = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
];
#e = [ "Ma" , "my ", "to!"];
f = "Dupa jaś";
while (b < 1000) {
    print b;
    b = b + a;
    a = b - a;
}

print c;
print d;
print f;
return b;