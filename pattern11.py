"""
Pattern 11

1 1 1 2 1 3
2 1 2 2 2 3
3 1 3 2 3 3
4 1 4 2 4 3
5 1 5 2 5 3

"""

for x in range(1, 6):
    for y in range(1, 4):
        print('{} {}'.format(x, y), end=' ')
    print()
    