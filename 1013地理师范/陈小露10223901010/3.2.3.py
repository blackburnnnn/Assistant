n=int(input('n='))
if n<=0:
    print('n输入错误！')
    exit(0)
a=2
b=1
s=0
for i in range(n):
    s=s+a/b
    a,b=b+a,a
print(f's={s:.2f}')
    
    
