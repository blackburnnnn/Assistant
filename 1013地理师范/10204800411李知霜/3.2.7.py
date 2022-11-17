k = 0
for a in range(0,4):
    for b in range(0,4):
        for c in range(0,4):
            if(a != b) and (b != c) and (a != c):
                num =(a*100+b*10+c)
                if len(str(num))== 3:
                    print(num)
                    k = k + 1
print("共{}个".format(k))
    
