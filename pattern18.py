'''
Pattern 18

0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0

'''

n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print('1', end=' ') if((i+j) % 2 != 0) else print('0', end=' ')
    print()
