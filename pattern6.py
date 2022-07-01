'''
Pattern 6

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

'''

n = 5
count = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        print("{:2d}". format(count), end=' ')
        count += 1
    print()
