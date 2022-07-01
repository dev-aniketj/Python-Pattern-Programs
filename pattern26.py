'''
Pattern 26

A A A A A
B B B B B
C C C C C
D D D D D
E E E E E

'''

n = 5
for i in range(65, 65+n):
    for j in range(n):
        print(chr(i), end=' ')
    print()
