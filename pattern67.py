"""
Pattern 67

E
E D
E D C
E D C B
E D C B A

"""

for i in range(69, 64, -1):
    for j in range(69, i-1, -1):
        print(chr(j), end=' ')
    print()
