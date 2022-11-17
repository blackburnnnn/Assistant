n=int(input('请输入行数'))
if n%2==0:
    n=n+1
i=1
while i<=n:
    m='*'
    if i==1 or i==n:
        m=m*7
        print(m)
    else:
        print('  ',m)
    i=i+1
        
