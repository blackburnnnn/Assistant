a=1
b=2
s=0
n=int(input('输入一个正整数'))
for n in range(1,n+1):
    s+=b/a
    a,b=b,a+b
print('前%d项的累加和为%f3'%(n,s))
