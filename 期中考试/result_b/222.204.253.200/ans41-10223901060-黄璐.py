x=int(input('请输入行数：'))
if x%2==0:
    x+=1
print('*'*x)
for i in range(1,x-1):
    print(''*(x//2+1),'*',''*(x//2+1))
print('*'*x)
