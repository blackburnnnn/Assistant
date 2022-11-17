n=int(input('请输入一个整数'))
if n<=0:
    print('n输出错误')
else:
    s=0
    a,b=2,1
    for i in range(n):
        s=s+a/b
        a=a+b
        b=a-b
    print(s)
