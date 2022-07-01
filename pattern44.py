'''
Pattern 44

 1
 3  2
 6  5  4
10  9  8  7
15 14 13 12 11

'''

n = 5
k = 0
for i in range(1, n+1):
    k += i
    for j in range(k, k-i, -1):
        print('{:2d}'.format(j), end=' ')
    print()
