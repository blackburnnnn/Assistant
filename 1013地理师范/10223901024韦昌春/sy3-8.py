#模拟角谷猜想过程，输出每一步变换结果，达到1停止。
n=int(input("n="))
while n!=1:
    if n%2==0:
        n=n/2
    else:
        n=3*n+1
    print(int(n),end=" ")
