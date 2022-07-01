'''
Pattern 40

2
2 4
2 4 6
2 4 6 8
2 4 6 8 10

'''

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j*2, end=' ')
    print()
