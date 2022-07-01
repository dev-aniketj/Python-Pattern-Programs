'''
Pattern 53

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

'''

n = 5
for i in range(1, n+1):
    t = 1
    for j in range(1, i+1):
        print(t, end=' ')
        t = t*(i-j)//j
    print()
