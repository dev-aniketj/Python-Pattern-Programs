"""
Pattern 68

E
D D
C C C
B B B B
A A A A A

"""

for i in range(69, 64, -1):
    for j in range(69, i-1, -1):
        print(chr(i), end=' ')
    print()
