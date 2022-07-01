'''
Pattern 16

 1  2  3  4  5
 2  3  4  5  6
 3  4  5  6  7
 4  5  6  7  8
 5  6  7  8  9

'''

n = 5
for i in range(0, n):
    for j in range(1, n+1):
        print('{:2d}'.format(i+j), end=' ')
    print()
