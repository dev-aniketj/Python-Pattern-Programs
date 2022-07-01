'''
Pattern 43

 1
 3  5
 5  7  9
 7  9 11 13
 9 11 13 15 17

'''

n = 5
for i in range(n):
    for j in range(i+1):
        print('{:2d}'.format((i+j)*2 + 1), end=' ')
    print()
