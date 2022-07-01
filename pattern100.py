'''
Pattern 100

        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1

'''

n = 5
for i in range(1, n+1):
    for j in range(n, 0, -1):
        print(j, end=' ') if i >= j else print(end='  ')
    print()
