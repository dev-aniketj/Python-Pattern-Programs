"""
Pattern 32

A F K P U
B G L Q V
C H M R W
D I N S X
E J O T Y

"""

for i in range(5):
    ch = 65 + i
    for j in range(5):
        print(chr(ch), end=' ')
        ch += 5
    print()
