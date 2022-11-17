a=input('输入一串转向指令:')
b='ENWS'
c=0
for i in a:
    if i=='L':
        c+=1
    elif i=='B':
        c+=2
    elif i==' ':
        c=c    
    else:
        c-=1
d=c%4
print('机器人面向;',b[d])
