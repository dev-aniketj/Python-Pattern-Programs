"""
Pattern 13

 1 10 11 20 21
 2  9 12 19 22
 3  8 13 18 23
 4  7 14 17 24
 5  6 15 16 25

"""

for i in range(1, 6):
    t1 = i
    t2 = 5 - i + 1
    for j in range(1, 6):
        if j % 2 == 1:
            print('{:2d}'.format(t1), end=' ')
        else:
            print('{:2d}'.format(t2), end=' ')
        t1 += 5
        t2 += 5
    print()
