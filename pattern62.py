'''
Pattern 62

0
0 1
0 1 0
0 1 0 1
0 1 0 1 0
0 1 0 1 0 1

'''

n = 5
for i in range(n+1):
    for j in range(i+1):
        print(j % 2, end=' ')
    print()
