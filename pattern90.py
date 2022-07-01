'''
Pattern 90

E D C B A
E D C B
E D C
E D
E

'''

n = 5
for i in range(n):
    for j in range(n-1, i-1, -1):
        print(chr(j+65), end=' ')
    print()
