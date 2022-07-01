'''
Pattern 68

E
D D
C C C
B B B B
A A A A A

'''

n = 5
for i in range(64+n, 64, -1):
    for j in range(64+n, i-1, -1):
        print(chr(i), end=' ')
    print()
