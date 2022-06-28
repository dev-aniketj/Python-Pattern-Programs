"""
Developer : Aniket Jain
Github : aniketjain8441
LinkedIn : www.linkedin.com/in/aniket-jain-80355a211/
"""

"""
Pattern 6

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

"""

count = 1
for x in range(1, 6):
    for y in range(1, 6):
        print("{:2d}". format(count), end=' ')
        count += 1
    print()
