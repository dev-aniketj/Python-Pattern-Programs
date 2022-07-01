'''
Pattern 95

        *
      * *
    * * *
  * * * *
* * * * *

'''

n = 5
for i in range(1, n+1):
    for j in range(n, 0, -1):
        print('*', end=' ') if i >= j else print(end='  ')
    print()
