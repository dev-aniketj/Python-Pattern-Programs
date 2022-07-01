'''
Pattern 11

 1  1  1  2  1  3
 2  1  2  2  2  3
 3  1  3  2  3  3
 4  1  4  2  4  3
 5  1  5  2  5  3

'''

n = 5
for i in range(1, n+1):
    for j in range(1, n-1):
        print('{:2d} {:2d}'.format(i, j), end=' ')
    print()
