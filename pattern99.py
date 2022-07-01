'''
Pattern 99

        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5

'''

n = 5
for i in range(n, 0, -1):
    for j in range(1, n+1):
        print(j, end=' ') if i <= j else print(end='  ')
    print()
