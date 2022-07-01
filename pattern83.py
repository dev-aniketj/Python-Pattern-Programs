'''
Pattern 83

1 0 1 0 1
1 0 1 0
1 0 1
1 0
1

'''

n = 5
for i in range(n):
    for j in range(n, i, -1):
        print(j % 2, end=' ')
    print()
