x=input('输入您的指令：')
a=len(x)
for i in range(a):
    if i=='N':
        s='N'
    elif i=='R':
        s='S'
    else:
        s='E'
print('最后机器面向：',s)
