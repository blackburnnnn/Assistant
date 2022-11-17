x=int(input('请输入行数:'))
while True:
    if x%2==1:
        x=x
    else:
        x+=1
    for i in range(x):
        if i==0 or i==x-1:
            print('*'*x,end='\n')
        else:
            a=int((x-1)/2)
            s=' '*a+'*'+' '*a
            print(s)
    break
