"""
Pattern 62

0
0 1
0 1 0
0 1 0 1
0 1 0 1 0
0 1 0 1 0 1

"""

for i in range(6):
    for j in range(i+1):
        print(j % 2, end=' ')
    print()
