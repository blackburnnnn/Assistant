l=int(input('请输入行数：'))
if l%2==0:
    l=l+1
a=(l-1)*1/2
print('*'*l)
if l%2!=0:
    for i in range(1,l-1):
        for j in range(0,l+1):
            if j==a:
                print('*',end='')
            else:
                print(' ',end='')
        print()
print('*'*l)
