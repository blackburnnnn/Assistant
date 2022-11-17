n=int(input("n="))
while n>1:
    if n%2==0:
        n=0.5*n
        print(n)
    elif n%2==1:
        n=3*n+1
        print(n)
