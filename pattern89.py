'''
Pattern 89

E E E E E
D D D D
C C C
B B
A

'''

n = 5
for i in range(n, 0, -1):
    for j in range(0, i):
        print(chr(64+i), end=' ')
    print()
