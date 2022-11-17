n=int(input("请输入一个正整数"))
while n!=1:
 if n==1:
    break
 if n%2==0:
    n=n//2
    print(str(n))
 else:
    n%2==1
    n=3*n+1
    print(str(n))
