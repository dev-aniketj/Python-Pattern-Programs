"""
Pattern 75

5 4 3 2 1
6 5 4 3
7 6 5
8 7
9

"""

for i in range(5):
    for j in range(5, i, -1):
        print(j+i, end=' ')
    print()
