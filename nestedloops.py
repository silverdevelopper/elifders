'''
1 2 3
4 5 6
7 8 9
'''
import random

matris = []
for i in range(3):
    r = []
    for j in range(3):
        #r.append(i*3+j+1)
        r.append(random.randint(1,100))
   # print(i,". ",r)
    matris.append(r)
# 3x3
for row in matris:
    for col in row:
        print(col,end=" ")
    print()
    