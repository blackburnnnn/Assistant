x=input('输入一串转向指令')
a='E'
for i in x:
    if a=='E':
        l,r,b='N','S','W'
    elif a=='N':
        l,r,b='W','E','S'
    elif a=='S':
        l,r,b='E','W','N'
    else:
        l,r,b='S','N','E'
        if i=='L':
            a=l
        if i=='R':
            a=r
        if i=='B':
            a=b
        else:
            a=a
print(f'最后机器人面向：{a}')
        
