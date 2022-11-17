n=int(input('n='))
if n<0:
    print('n输入错误')
    exit(0)
s=0
for i in range(1,n+1):
    x=1
    for j in range(1,i+1):
        x=x*j
    s=s+x
print('阶乘的和为：',s)
