'''
Pattern 54

1
1 2
2 3 4
4 5 6 7
7 8 9 10 11

'''

n = 5
t = 1
for i in range(0, n):
    for j in range(0, i+1):
        print(t-i, end=' ')
        t += 1
    print()
