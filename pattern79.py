'''
Pattern 79

17 18 19 20
14 15 16
12 13
11

'''

n = 4
count = (n*n) + 1
for i in range(n, 0, -1):
    for j in range(i):
        print('{:2d}'.format(count), end=' ')
        count += 1
    count -= 1
    count = count - ((i-1)*2)
    print()
