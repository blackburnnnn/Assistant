x=int(input('请输入行数：'))
if x%2==0:
    x+=1
else:
    x=x
for i in range(1,x+1):
    if i==1:
        for j in range(x):
            print('*',end='')
    if 1<i<x:
        for t in range(1,x+1):
            if t!=(x+1)/2:
                print(' ',end='')
            else:
                print('*',end='')
    if i==x:
       for h in range(x):
            print('*',end='')
