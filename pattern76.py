"""
Pattern 76

5 6 7 8 9
4 5 6 7
3 4 5
2 3
1

"""

for i in range(1, 6):
    for j in range(1, 5-i+2):
        print(5-i+j, end=' ')
    print()
