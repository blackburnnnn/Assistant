x=int(input('请输入行数：'))
for i in range(0,x+2):
    if i==0 or i ==x:
        for b in range(0,x-1):
             print('*',end=(''))
    else:
        print('*')
