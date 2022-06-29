"""
Pattern 31

A B C D E
B C D E F
C D E F G
D E F G H
E F G H I

"""

ch = 65
for i in range(5):
    for j in range(5):
        print(chr(ch+j), end=' ')
    print()
    ch += 1
