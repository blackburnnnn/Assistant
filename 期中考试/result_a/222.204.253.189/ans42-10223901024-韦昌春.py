a=input('输入一串转向指令')
s1=a.split()
x,y,z=0,0,0
for i in a:
    if i=='R':
        x+=1
    elif i=='L':
        y+=1
    elif i=='B':
        z+=1
n=x-y+2*z
if n%4==0:
    print('最后机器人面向：E')
if n%4==1 or n==1:
    print('最后机器人面向：S')
if n%4==2 or n==2:
    print('最后机器人面向：W')
if n%4==3 or n==3:
    print('最后机器人面向：N')
