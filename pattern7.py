"""
Developer : Aniket Jain
Github : aniketjain8441
LinkedIn : www.linkedin.com/in/aniket-jain-80355a211/
"""

"""
Pattern 7

 1  3  5  7  9
11 13 15 17 19
21 23 25 27 29
31 33 35 37 39
41 43 45 47 49

"""

count = 1
for x in range(1, 6):
    for y in range(1, 6):
        print('{:2d}'.format(count), end=' ')
        count += 2
    print()
