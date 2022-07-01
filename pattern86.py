'''
Pattern 86

1 0 1 0 1
0 1 0 1
1 0 1
0 1
1

'''

n = 5
for i in range(n):
    for j in range(n, i, -1):
        print((i+j) % 2, end=' ')
    print()
