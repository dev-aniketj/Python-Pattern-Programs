'''
Pattern 69

A
B A
C B A
D C B A
E D C B A

'''

n = 5
for i in range(n):
    for j in range(i, -1, -1):
        print(chr(j+65), end=' ')
    print()
