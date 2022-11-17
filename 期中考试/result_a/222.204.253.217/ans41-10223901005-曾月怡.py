l=int(input('请输入行数：'))
a=(l-1)*1/2
b=(l-3)*1/2
print('*'*l)
if l%2==0:
    l=l+1
for i in range (1,l-1):
    for j in range (1,l):
        if j==a:
            print('*',end='')
        else:
            print(' '*int(b),end='')
    print()
print('*'*l)
