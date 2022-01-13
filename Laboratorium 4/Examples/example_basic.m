A = 10;
B = [1, 3, 4];
D = [[1,0],
    [0,2],
    [0,2]];
{
    B = 5;
    C = A + B;
}
#C = A + B;

B[2] = 1;
D[2,1] = 2;
N = 5;
M = 10;
i = [9,6];
for i = 1:N {
    x = i + 1;
    for j = i:M {
        continue;
        j = i;
    }
    break;
}

i = [0];

{
    i = 7;
    j = i + 7;
}

i += j;