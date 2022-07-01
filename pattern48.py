'''
Pattern 48

 1
 6  2
10  7  3
13 11  8  4
15 14 12  9  5

'''

n = 5
a = 1
for i in range(n, 0, -1):
    b = i
    t = a
    for j in range(n+1, i, -1):
        print('{:2d}'.format(t), end=' ')
        t = t - b
        b += 1
    a = a + i
    print()
