#求分数序列的和
n=int(input('请输入一个整数n='))
y=2
x=1
total=0
if n>0:
    for n in range(1,n+1):
        total=total+y/x
        x=x+y
        x,y=y,x 
else:
    print('n输入错误')

print("这个分数序列前",n,"项的和是",total)
