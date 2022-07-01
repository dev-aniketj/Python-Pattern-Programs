'''
Pattern 77

 1  2  3  4  5
 6  7  8  9
10 11 12
13 14
15

'''

n = 5
count = 1
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('{:2d}'.format(count), end=' ')
        count += 1
    print()
