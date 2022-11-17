import math
s=0
for i in range(1,9+1):
    for j in range(1,9+1):
        if i>=j:
          s=i*j
          print("{:.1f}*{:.1f}={:.1f}".format(i,j,s),end="  ")
    print()
        
