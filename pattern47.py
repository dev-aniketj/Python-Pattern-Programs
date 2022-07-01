'''
Pattern 47

 1
 2  4
 3  6  9
 4  8 12 16
 5 10 15 20 25

'''

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print('{:2d}'.format(i*j), end=' ')
    print()
