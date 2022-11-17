a= int(input('请输入行数：'))
if a%2==0:
    a+=1
    b=a-2
    c=a//2
    m=' '*(c+1)+'*\n'
    print('*'*a)
    print(m*b)
    print('*'*a)
else:
    b=a-2
    c=a//2
    m=' '*(c+1)+'*\n'
    print('*'*a)
    print(m*b)
    print('*'*a)
