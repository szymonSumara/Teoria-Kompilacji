x = 0;
m = x[9];
y = zeros(5);
z = x + y;
h = m;

x = eye(5);
y = eye(8);
z = x + y;

x = [ 1,2,3,4,5 ];
y = [ [1,2,3,4,5],
      [1,2,3,4,5] ];
z = x + y;

x[3] = "zaba";



x = zeros(5);
y = zeros(5,7);
z = x + y;

x = ones(3,5);
z = x[7,10];
v = x[2,3,4];

a = zeros(5);
b = zeros(2, 5);

c = a * b;
d = a * b';

e = d + x;