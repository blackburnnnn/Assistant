a=int(input('请输入行数：'))
if a%2==0:
    a=a+1
print('*'*a)
for i in range(a):
    print(''*a,'*')
print('*'*a)
