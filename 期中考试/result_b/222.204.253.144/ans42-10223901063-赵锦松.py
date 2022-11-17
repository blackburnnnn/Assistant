ss=input("输入一串转向指令:")
n=1
if ss!="":
    for i in ss:
        if i=="L":
            n+=1
        elif i=="B":
            n+=2
        elif i=="R":
            n+=3
    if (n+4)%4==1:
        print("E")
    elif (n+4)%4==2:
        print("N")
    elif (n+4)%4==3:
        print("W")
    elif n%4==0:
        print("S")
else:
    print("E")
