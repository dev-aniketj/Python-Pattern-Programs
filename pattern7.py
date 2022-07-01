'''
Pattern 7

 1  3  5  7  9
11 13 15 17 19
21 23 25 27 29
31 33 35 37 39
41 43 45 47 49

'''

n = 5
count = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        print('{:2d}'.format(count), end=' ')
        count += 2
    print()
