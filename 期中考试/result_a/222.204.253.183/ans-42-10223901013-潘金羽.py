x=input("输入一串指令:")
a="E"
count=0
if x=='':
    print("最后机器人面向:E")
else:
    for i in 'x':
        if i=="L":
            count+=1
        if i=="R":
            count-=1
        if i=="B":
            count+=2
            
            
            
            

