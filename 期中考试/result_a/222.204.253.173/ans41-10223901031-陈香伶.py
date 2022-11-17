x=int(input('请输入行数:'))
if x%2!=0:
    x=x
else:
    x=x+1
print('*'*x)
b=int((x-1)/2)
for i in range(1,x-1):
    print(' '*b+'*'+' '*b)
print('*'*x)
