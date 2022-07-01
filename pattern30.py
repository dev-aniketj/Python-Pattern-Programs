'''
Pattern 30

A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y

'''

ch = 65
n = 5
for i in range(n):
    for j in range(n):
        print(chr(ch), end=' ')
        ch += 1
    print()
