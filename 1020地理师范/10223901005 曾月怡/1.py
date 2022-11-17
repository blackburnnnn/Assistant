for s in range (1,100):
    for g in range (1,100):
        m=100-s-g 
        if (s%3+g*2+m*3==100)and s%3==0 and m>=0:
            print("母鸡，公鸡，小鸡的数目分别为",m,g,s)
