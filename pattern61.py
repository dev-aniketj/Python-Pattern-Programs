"""
Pattern 61

1
1 0
1 0 1
1 0 1 0
1 0 1 0 1

"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(j % 2, end=' ')
    print()
