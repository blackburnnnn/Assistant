n='E'
a=input("输入一串转向指令")
for i in a:
    if i =='L':
        n='S'
    elif i=='R':
        n='N'
    elif i=='B':
        n='W'
    else:
        n='E'
print("最后机器人面向:",n)
        
    
