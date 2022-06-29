"""
Pattern 59

1
0 0
1 1 1
0 0 0 0
1 1 1 1 1

"""

for i in range(1, 6):
    for j in range(i):
        print(i % 2, end=' ')
    print()
