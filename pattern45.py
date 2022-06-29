"""
Pattern 45

 1
 3  5
 7  9 11
13 15 17 19
21 23 25 27 29

"""

k = 1
for i in range(1, 6):
    for j in range(i):
        print('{:2d}'.format(k), end=' ')
        k += 2
    print()
