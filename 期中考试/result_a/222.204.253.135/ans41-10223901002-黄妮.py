n=int(input('请输入行数：'))
if n%2==0:
    n+=1
for i in range (n):
    if i==0 or i==n-1:
        for a in range (n):
            print('*',end='')
    else:
        for b in range (n):
            if b==n//2:
                print('*',end='')
            else:
                print(' ',end='')
