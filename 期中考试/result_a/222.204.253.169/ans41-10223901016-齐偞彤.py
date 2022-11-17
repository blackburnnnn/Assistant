a=int(input('请输入行数：'))
if a%2==0:
    a=a+1
for i in range(1,a+1):
    b=int((a-1)/2)
    if i==1 or i==a:
        print('*'*a)
    else:
        print(' '*b+'*'+' '*b)
    
    
