'''
Pattern 93

E F G H I
D E F G
C D E
B C
A

'''

n = 5
for i in range(n, 0, -1):
    ch = 64+i
    for j in range(i, 0, -1):
        print(chr(ch), end=' ')
        ch += 1
    print()
