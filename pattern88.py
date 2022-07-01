'''
Pattern 88

A B C D E
A B C D
A B C
A B
A

'''

n = 5
for i in range(n, 0, -1):
    for j in range(0, i):
        print(chr(65+j), end=' ')
    print()
