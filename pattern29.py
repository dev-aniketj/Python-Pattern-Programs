'''
Pattern 29

E D C B A
E D C B A
E D C B A
E D C B A
E D C B A

'''

n = 5
for i in range(n):
    for j in range(65+n-1, 64, -1):
        print(chr(j), end=' ')
    print()
