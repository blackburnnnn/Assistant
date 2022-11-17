a=input('输入一串转向指令')
m,n=0,0
for x in a:
    if x=='L':
        m+=1
    if x=='R':
        m+=3
    if x=='B':
        m+=2
n=m%4
if n==0:
    print('最后机器人面向：E')
if n==1:
    print('最后机器人面向：N')
if n==2:
    print('最后机器人面向：W')
if n==3:
    print('最后机器人面向：S')

    
