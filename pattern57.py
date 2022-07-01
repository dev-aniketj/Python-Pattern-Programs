'''
Pattern 57 (Fibonacci Series)

  0
  1   1
  2   3   5
  8  13  21  34
 55  89 144 233 377

'''

n = 5
n1, n2 = 0, 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print('{:3d}'.format(n1), end=' ')
        temp = n2
        n2 += n1
        n1 = temp
    print()
