for a in range(1,99):
    for b in range(1,100-a):
        c=100-a-b
        if a*3+b*2+c*1/3==100 and c%3==0:
            print(f"公鸡{a}只，母鸡{b}只，小鸡{c}只")
        
