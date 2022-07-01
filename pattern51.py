'''
Pattern 51

15
14 13
12 11 10
 9  8  7  6
 5  4  3  2  1

'''

n = 5
count = (n*(n+1)) // 2
for i in range(n, 0, -1):
    for j in range(n, i-1, -1):
        print('{:2d}'.format(count), end=' ')
        count -= 1
    print()
