"""
Pattern 14

 5 10 15 20 25
 4  9 14 19 24
 3  8 13 18 23
 2  7 12 17 22
 1  6 11 16 21

"""

for i in range(1, 6):
    t1 = 5 - i + 1
    for j in range(1, 6):
        print('{:2d}'.format(t1), end=' ')
        t1 += 5
    print()
