a=int(input('请输入行数：'))
l=(a-1)*(1/2)
print('*'*a)
if a%2==0:
    a=a+1
for i in range(0,a-2):
    for j in range(0,a):
        if j==i:
            print('   *',end='')
        else :
            print('',end='')
    print()
print('*'*a)

      
