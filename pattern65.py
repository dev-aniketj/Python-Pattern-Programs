'''
Pattern 65

A
B B
C C C
D D D D
E E E E E

'''

n = 5
for i in range(65, 65+n):
    for j in range(64, i):
        print(chr(i), end=' ')
    print()
