'''
Pattern 74

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

'''

n = 5
for i in range(n):
    for j in range(n, i, -1):
        print(j, end=' ')
    print()
