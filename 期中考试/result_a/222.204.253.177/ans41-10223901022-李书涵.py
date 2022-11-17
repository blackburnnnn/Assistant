a=int(input('请输入行数：'))
if a%2==0:
   a+=1
for i in range(0,a+2):
    if i==0 or i ==a:
        for b in range(0,a-1):
           print('*',end=(''))
    else:
        print('*')
    
