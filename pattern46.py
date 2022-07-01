'''
Pattern 46

 2
 4  6
 8 10 12
14 16 18 20
22 24 26 28 30

'''

n = 5
k = 0
for i in range(1, n+1):
    for j in range(i):
        k += 2
        print('{:2d}'.format(k), end=' ')
    print()
