a=input('请输入一串转向指令：')
b=['E','S','W','N']
n=0
for i in a:
    if i=='L':
        n=n-1
        if n<0:
            n=n+4
    if i=='R':
        n=n+1
        if n>3:
            n=n-4
    if i=='B':
        n=n+2
        if n>3:
            n=n-4
print(b[n])
            
    
    
