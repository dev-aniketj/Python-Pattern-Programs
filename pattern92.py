'''
Pattern 92

E D C B A
F E D C
G F E
H G
I

'''

n = 5
for i in range(n):
    ch = 64+n+i
    for j in range(n, i, -1):
        print(chr(ch), end=' ')
        ch -= 1
    print()
