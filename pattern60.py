"""
Pattern 60

0
1 1
0 0 0
1 1 1 1
0 0 0 0 0

"""

for i in range(5):
    for j in range(i+1):
        print(i % 2, end=' ')
    print()
