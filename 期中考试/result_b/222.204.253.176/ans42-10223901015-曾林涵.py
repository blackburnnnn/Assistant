x=input('输入一串转向指令')
a=0
for i in x:
    if i=='R':
        a+=1
    if i=='L':
        a-=1
    if i=='B':
        a+=2

b=a%4
if b ==0:
    print('最后机器人面向：E')
elif b == 1:
    print('最后机器人面向：S')
elif b == 2:
    print('最后机器人面向：W')
elif b == 3:
    print('最后机器人面向：N')
    
