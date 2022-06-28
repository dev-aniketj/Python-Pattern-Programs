"""
Pattern 12

 1  6 11 16 21
 2  7 12 17 22
 3  8 13 18 23
 4  9 14 19 24
 5 10 15 20 25

"""

for x in range(1, 6):
    count = x
    for y in range(1, 6):
        print('{:2d}'.format(count), end=' ')
        count += 5
    print()
