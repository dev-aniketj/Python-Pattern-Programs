'''
Pattern 22

0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0

'''

n = 5
for i in range(0, n):
    for j in range(1, n+1):
        print(i % 2, end=' ')
    print()
