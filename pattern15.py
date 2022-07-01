'''
Pattern 15

 5  6 15 16 25
 4  7 14 17 24
 3  8 13 18 23
 2  9 12 19 22
 1 10 11 20 21

'''

n = 5
for i in range(1, n+1):
    t1 = 5 - i + 1
    t2 = i
    for j in range(1, n+1):
        if j % 2 == 1:
            print('{:2d}'.format(t1), end=' ')
        else:
            print('{:2d}'.format(t2), end=' ')
        t1 += 5
        t2 += 5
    print()
