"""
Pattern 25

0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0

"""

for i in range(1, 6):
    for j in range(1, 6):
        print(j % 2, end=' ')
    print()
