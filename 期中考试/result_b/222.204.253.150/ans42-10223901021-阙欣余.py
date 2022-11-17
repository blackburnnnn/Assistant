a=input('请输入一串转向指令')
b=0
if a=='':
   print('最后机器人面向：E')
else:
    for x in a:
        if x=='L':
           b=b+1
        if x=='R':
           b=b-1
        if x=='B':
           b=b+2
    if b==2 or b==-2:
         print('最后机器人朝向：W')
    elif b%4==0:
         print('最后机器人朝向：E')
    elif b==-3 or b==1:
         print('最后机器人朝向：N')
    else:
         print('最后机器人朝向：S')
