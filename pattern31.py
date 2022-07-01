'''
Pattern 31

A B C D E
B C D E F
C D E F G
D E F G H
E F G H I

'''

ch = 65
n = 5
for i in range(n):
    for j in range(n):
        print(chr(ch+j), end=' ')
    print()
    ch += 1
