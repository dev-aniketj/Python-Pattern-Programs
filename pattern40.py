"""
Pattern 40

2
2 4
2 4 6
2 4 6 8
2 4 6 8 10

"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(j*2, end=' ')
    print()
