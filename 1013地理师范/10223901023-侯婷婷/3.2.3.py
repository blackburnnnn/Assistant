n=int(input('请输入一个人正整数：'))
if n<=0:
    print('n输入错误')
else:
    a=1
    b=2
    sum=0
    for i in range(n):
        a=b
        b=a+b
        sum=sum+b/a
    print("前n 项的和为",sum)
