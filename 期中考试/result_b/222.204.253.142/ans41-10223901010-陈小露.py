x=int(input('请输入行数:'))
if x%2==0:
    x+=1
for i in range(x):
    if i==0 or i==x-1:
        for j in range(x):
            print('*',end='')
        print('')
    else:
        for n in range((int(x)-1)//2):
            print(' ',end='')
        print('*',end='')
        for n in range((int(x)-1)//2):
            print(' ',end='')
        print('')
