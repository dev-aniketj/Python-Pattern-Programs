'''
Pattern 81

1 1 1 1 1
0 0 0 0
1 1 1
0 0
1

'''

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i % 2, end=' ')
    print()
