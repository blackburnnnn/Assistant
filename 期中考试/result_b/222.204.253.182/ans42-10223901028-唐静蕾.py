x=str(input('输入一串转向指令'))
d=E
for i in range(x):
    if i==L:
        E,N,W,S=N,W,S,E
    if i==R:
        E,N,W,S=S,E,N,W
    if i==B:
        E,N,W,S=W,S,E,N
        break
    print('最后机器人面向：{}'.format(d))
