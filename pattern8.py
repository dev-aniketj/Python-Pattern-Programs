"""
Pattern 8

 2  4  6  8 10
12 14 16 18 20
22 24 26 28 30
32 34 36 38 40
42 44 46 48 50

"""

count = 2
for x in range(1, 6):
    for y in range(1, 6):
        print('{:2d}'.format(count), end=' ')
        count += 2
    print()
    