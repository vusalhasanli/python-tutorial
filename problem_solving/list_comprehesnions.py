#print a list of all possible coordinates given by (i, j, k) on a 3D grid 
#where the sum of (i + j + k) is not equal to N

# i = 1; x = 2
# j = 2; y = 3
# k = 0; z = 1
# n = 3
x, y, z, n = (int(input()) for _ in range(4))
print([ [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range( z + 1) if ( i + j + k != n)])

