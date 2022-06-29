"""
Pattern 64

1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

"""

for i in range(1, 6):
    for j in range(i):
        print((i+j) % 2, end=' ')
    print()
