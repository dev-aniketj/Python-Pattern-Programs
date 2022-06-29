"""
Pattern 17

 1  3  5  7  9
 3  5  7  9 11
 5  7  9 11 13
 7  9 11 13 15
 9 11 13 15 17

"""

for i in range(1, 6):
    for j in range(1, 6):
        print('{:2d}'.format(2 * (i+j) - 3), end=' ')
    print()
