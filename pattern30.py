"""
Pattern 30

A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y

"""

ch = 65
for i in range(5):
    for j in range(5):
        print(chr(ch), end=' ')
        ch += 1
    print()
