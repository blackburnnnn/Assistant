x=input('输入一串转向指令')
s,n=1,0
y=''
for i in x:
    if i=='L':
            s=s+1
    elif i=='R':
            s=s+3
    elif i=='B':
            s=s+2
    else:
            s=s
n=s%4
if n==1:
    y='E'
elif n==2:
    y='N'
elif n==3:
    y='W'
else:
    y='S'
print('最后机器人面向：{}'.format(y))
    

            
    
