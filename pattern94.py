'''
Pattern 94

A
B C
D E F
G H I J
K L M N O

'''

n = 5
ch = 65
for i in range(5):
    for j in range(i+1, 0, -1):
        print(chr(ch), end=' ')
        ch += 1
    print()
