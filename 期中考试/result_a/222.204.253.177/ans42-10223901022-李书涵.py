a=input('输入一串转向指令')
b=0
for i in a:
    if i=='R':
        b+=1
    if i=='L':
        b-=1
    if i=='B':
        b+=2

c=b%4
if c ==0:
    print('最后机器人面向：E')
elif c == 1:
    print('最后机器人面向：S')
elif c == 2:
    print('最后机器人面向：W')
elif c ==3:
    print('最后机器人面向：N')
