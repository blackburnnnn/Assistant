n=input('请输入一串转向指令')
s1,s2=0,0
for i in n:
    
    if i=='R':
        s1=s1+1
    if i=='L':
        s2=s2+1
m=(s1-s2)%4
if m==0:
    h='E'
elif m==1 or m==-3:
    h='S'
elif m==2 or m==-2:
    h='W'
elif m==3 or m==-1:
    h='N'
print('最后机器人面向:',h)
