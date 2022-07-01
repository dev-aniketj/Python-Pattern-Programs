'''
Pattern 52

 5
 9  4
12  8  3
14 11  7  2
15 13 10  6  1

'''

n = 5
d = n
for i in range(n, 0, -1):
    t = d
    e = i+1
    for j in range(n, i-1, -1):
        print('{:2d}'.format(t), end=' ')
        t = t-e
        e += 1
    d = d+i-1
    print()
