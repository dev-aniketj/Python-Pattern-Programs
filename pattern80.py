'''
Pattern 80

 5  9 12 14 15
 4  8 11 13
 3  7 10
 2  6
 1

'''

n = 5
for i in range(n, 0, -1):
    count = i
    for j in range(1, i+1):
        print('{:2d}'.format(count), end=' ')
        count += n-j
    print()
