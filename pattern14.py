'''
Pattern 14

 5 10 15 20 25
 4  9 14 19 24
 3  8 13 18 23
 2  7 12 17 22
 1  6 11 16 21

'''

n = 5
for i in range(1, n+1):
    t1 = 5 - i + 1
    for j in range(1, n+1):
        print('{:2d}'.format(t1), end=' ')
        t1 += 5
    print()
