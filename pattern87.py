'''
Pattern 87

A A A A A
B B B B
C C C
D D
E

'''

n = 5
for i in range(n):
    for j in range(n, i, -1):
        print(chr(i+65), end=' ')
    print()
