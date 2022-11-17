a=input('输入一串转向指令')
x=0
for i in a :
    if i=='L':
        x+=3
    if i=='R':
        x+=1
    if i=='B':
        x+=2
if  x%4==1:
    print('S')
elif x%4==2:
    print('W')
elif x%4==3:
    print('N')
else :
    print('R')
    
