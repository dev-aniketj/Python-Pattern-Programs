'''
Pattern 24

0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0

'''

n = 5
for i in range(1, n+1):
    for j in range(0, n):
        print(j % 2, end=' ')
    print()
