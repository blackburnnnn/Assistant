n=int(input('请输入行数：'))
count=1
count2=1
if n%2==1:
    n=n+1
    k=int((n+1)/2)
else:
    n=n+2
    k=int((n+1)/2)
if count==1:
    for i in range(1,n):
        print('*',end='')
    count+=1
print('')
for count2 in range(1,n-2):
    for count in range(2,k+1):
        print(' ',end='')
        count+=1
    if count==k+1:
        print('*',end='')
        count+=1
    for count in range(k+2,n):
        print(' ',end='')
        count+=1
    print('')
    count2+=1
if count==n:
    for i in range(1,n):
        print('*',end='')

