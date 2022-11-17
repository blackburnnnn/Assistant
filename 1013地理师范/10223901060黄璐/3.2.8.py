N=input("n=")
n=eval(N)
for i in range(1,100):
    if n%2==0:
        n=n/2
        print(n,end=" ")
    else:
        n=3*n+1
        print(n,end=" ")
    i+=1
    while n==1:
        quit()
