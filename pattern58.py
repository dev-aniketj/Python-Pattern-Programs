'''
Pattern 58 (Fibonacci Pyramid)

 0
 0  1
 0  1  1
 0  1  1  2
 0  1  1  2  3

'''

n = 5
for i in range(1, n+1):
    n1, n2 = 0, 1
    for j in range(1, i+1):
        print('{:2d}'.format(n1), end=' ')
        temp = n2
        n2 += n1
        n1 = temp
    print()
