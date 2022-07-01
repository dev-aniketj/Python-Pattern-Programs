'''
Pattern 27

A B C D E
A B C D E
A B C D E
A B C D E
A B C D E

'''

n = 5
for i in range(n):
    for j in range(65, 65+n):
        print(chr(j), end=' ')
    print()
