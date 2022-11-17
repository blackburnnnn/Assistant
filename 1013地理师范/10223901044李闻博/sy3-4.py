#判断完数
for n in range(2,1001):
    total=1
    for i in range(2,n):
        if n%i==0:
            total+=i
    if total==n:
        print(n)
L=[6,28,496]       
s=len(L)
print('1000之内共有',s,'个完数')
