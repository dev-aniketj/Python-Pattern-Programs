'''
Pattern 33

E J O T Y
D I N S X
C H M R W
B G L Q V
A F K P U

'''

n = 5
for i in range(1, n+1):
    ch = 65
    for j in range(n):
        print(chr(ch + n - i), end=' ')
        ch += n
    print()
