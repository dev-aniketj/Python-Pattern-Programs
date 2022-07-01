'''
Pattern 55

  1
  4   9
 16  25  36
 49  64  81 100

'''

n = 4
count = 1
for i in range(n):
    for j in range(i+1):
        print('{:3d}'.format(pow(count, 2)), end=' ')
        count += 1
    print()
