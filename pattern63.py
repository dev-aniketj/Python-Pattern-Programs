"""
Pattern 63

0
1 0
0 1 0
1 0 1 0
0 1 0 1 0

"""

for i in range(5):
    for j in range(i+1):
        print((i+j) % 2, end=' ')
    print()
