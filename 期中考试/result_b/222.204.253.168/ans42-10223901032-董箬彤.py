x=input("输入一串转向指令")
if x==" ":
    print("最后机器人面向： E")
else:
    for i in x:
        y=0
        if i=="L":
            i=3
        elif i=="R":
            i=1
        elif i=="B":
            i=2
        y += i
    if y%4==0:
        print("最后机器人面向： E")
    elif y%4==1:
        print("最后机器人面向： S")
    elif y%4==2:
        print("最后机器人面向： W")
    elif y%4==3:
        print("最后机器人面向： N")


        
