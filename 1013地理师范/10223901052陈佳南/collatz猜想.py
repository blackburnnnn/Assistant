n=int(input("请输入一个数"))
for i in range(1,50):
 if n%2==0:
    n=n/2
    print(n,end=" ")
 else:
    n=n*3+1
    print(n,end=" ")
 while n==1:
       quit()
