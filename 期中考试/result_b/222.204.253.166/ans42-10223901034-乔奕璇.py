x=input("输入一串转向指令")
if x == " ":
    print("最后机器人面向：E")
else:
    n=0
    for i in x:
        if i == "R":
            n=n+1
        if i == "L":
            n=n-1
        if i == "B":
            n=n+2
    if n == 0:
        print("最后机器人面向：E")
    if n > 0:
        if n % 3 == 0:
            print("最后机器人面向：N")
        elif n % 2 == 0:
            print("最后机器人面向：W")
        else:
            print("最后机器人面向：S")
    if n < 0:
        if n % 3 == 0:
            print("最后机器人面向：S")
        elif n % 2 == 0:
            print("最后机器人面向：W")
        else:
            print("最后机器人面向：N")
        
        
        
        
    
            
    
