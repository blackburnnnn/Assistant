x=str(input('输入一串转向指令'))
for i in x:
    a=0
    if i=='L':
        a-=1
    if i=='R':
        a=+1
    if i=='B':
        a+=2
if a%4==0:
    print('最后机器人面向E')
if a%4==1:
    print('最后机器人面向N')
if a%4==2:
    print('最后机器人面向W')
if a%4==3:
    print('最后机器人面向S')
        
        
