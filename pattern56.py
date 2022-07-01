'''
Pattern 56

 1
 2  6
 3  7 10
 4  8 11 13
 5  9 12 14 15

'''

n = 5
for i in range(1, n+1):
    a = i
    b = 4
    for j in range(1, i+1):
        print('{:2d}'.format(a), end=' ')
        a = a+b
        b -= 1
    print()
