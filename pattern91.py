'''
Pattern 91

E D C B A
D C B A
C B A
B A
A

'''

n = 5
for i in range(n, 0, -1):
    ch = 64+i
    for j in range(i, 0, -1):
        print(chr(ch), end=' ')
        ch -= 1
    print()
