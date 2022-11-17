l=int(input("请输入行数："))
a=(l-1)*(1/2)
print("*"*l)
if 1%2==0:
    l=l+1
for i in range (0,l-2):
    for j in range (0,l):
        if j==i:
            print('   *',end='')
        else:
            print('',end='')
    print()
print('*'*l)
