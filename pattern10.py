"""
Developer : Aniket Jain
Github : aniketjain8441
LinkedIn : www.linkedin.com/in/aniket-jain-80355a211/
"""

"""
Pattern 10

1 1 2 1 3 1
1 2 2 2 3 2
1 3 2 3 3 3
1 4 2 4 3 4
1 5 2 5 3 5

"""

for x in range(1, 6):
    for y in range(1, 4):
        print('{} {}'.format(y,x), end=' ')
    print()
