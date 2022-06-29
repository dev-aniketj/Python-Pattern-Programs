"""
Pattern 33

E J O T Y
D I N S X
C H M R W
B G L Q V
A F K P U

"""

for i in range(1, 6):
    ch = 65
    for j in range(5):
        print(chr(ch + 5 - i), end=' ')
        ch += 5
    print()
