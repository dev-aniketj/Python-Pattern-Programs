"""
Pattern 22

0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0

"""

for i in range(0, 5):
    for j in range(1, 6):
        print(i % 2, end=' ')
    print()
