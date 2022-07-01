'''
Pattern 28

E E E E E
D D D D D
B B B B B
C C C C C
A A A A A

'''

n = 5
for i in range(65+n-1, 64, -1):
    for j in range(n):
        print(chr(i), end=' ')
    print()
