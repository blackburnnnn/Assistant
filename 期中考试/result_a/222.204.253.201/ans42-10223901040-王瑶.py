a=input("输入一串转向指令")
p=0
for i in a:
    if i=="L":
        p+=1
    if i=="R":
        p+=3
    if i=="B":
        p+=2
if p%4==0:
    f='E'
if p%4==1:
    f='N'
if p%4==2:
    f='W'
if p%4==3:
    f='S'
print('最后机器人面向：',f)
        
