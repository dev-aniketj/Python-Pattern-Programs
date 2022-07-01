'''
Pattern 84

0 1 0 1 0
0 1 0 1
0 1 0
0 1
0

'''

n = 5
for i in range(n, 0, -1):
    for j in range(0, i):
        print(j % 2, end=' ')
    print()
