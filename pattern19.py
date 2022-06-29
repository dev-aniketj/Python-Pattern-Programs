"""
Pattern 19

1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1

"""

for i in range(1, 6):
    for j in range(1, 6):
        if((i+j) % 2 == 0):
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()
