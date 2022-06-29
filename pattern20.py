"""
Pattern 20

1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1

"""

for i in range(1, 6):
    for j in range(1, 6):
        print((i*j) % 2, end=' ')
    print()
