a=1
b=2
s=0
n=int(input())
for n in range(1,n+1):
   s+=b/a
   a,b=b,a+b
if n>0:
  print('前%d项的累加和为%.2f'%(n,s))

else:   
  print('n输入错误')
        
