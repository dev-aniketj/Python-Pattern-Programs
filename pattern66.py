'''
Pattern 66

A
A B
A B C
A B C D
A B C D E

'''

n = 5
for i in range(65, 65+n):
    for j in range(65, i+1):
        print(chr(j), end=' ')
    print()
