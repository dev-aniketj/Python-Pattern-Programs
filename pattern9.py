"""
Pattern 9

 1  2  3  4  5
 2  4  6  8 10
 3  6  9 12 15
 4  8 12 16 20
 5 10 15 20 25

"""

for x in range(1, 6):
    for y in range(1, 6):
        print('{:2d}'.format(x*y), end=' ')
    print()
