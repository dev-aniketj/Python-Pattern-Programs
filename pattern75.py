'''
Pattern 75

5 4 3 2 1
6 5 4 3
7 6 5
8 7
9

'''

n = 5
for i in range(n):
    for j in range(n, i, -1):
        print(j+i, end=' ')
    print()
