'''
Pattern 32

A F K P U
B G L Q V
C H M R W
D I N S X
E J O T Y

'''

n = 5
for i in range(n):
    ch = 65 + i
    for j in range(n):
        print(chr(ch), end=' ')
        ch += n
    print()
