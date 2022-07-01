'''
Pattern 76

5 6 7 8 9
4 5 6 7
3 4 5
2 3
1

'''

n = 5
for i in range(1, n+1):
    for j in range(1, n-i+2):
        print(n-i+j, end=' ')
    print()
