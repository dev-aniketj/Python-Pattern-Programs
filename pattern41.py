'''
Pattern 41

 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15

'''

n = 5
count = 1
for i in range(n):
    for j in range(i+1):
        print('{:2d}'.format(count), end=' ')
        count += 1
    print()
