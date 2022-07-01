'''
Pattern 67

E
E D
E D C
E D C B
E D C B A

'''

n = 5
for i in range(64+n, 64, -1):
    for j in range(64+n, i-1, -1):
        print(chr(j), end=' ')
    print()
