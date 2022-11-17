s=input('输入一串转向指令')
a=0
for i in s:
    if i=='R':
        a+=1
    elif i=='B':
        a+=2
    elif i=='L':
        a+=3
if a%4==0:
            print('E')
elif a%4==1:
            print('S')
elif a%4==2:
            print('W')
elif a%4==3:
            print('N')
