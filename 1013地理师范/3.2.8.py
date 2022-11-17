n=int(input("n="))
print('%d'%n)
while n!=1:
    if n%2==0:
        k=n/2
        n=k
        print('%d'%n)
    elif n==1:
        print('%d'%n)
        break
    else:
        g=3*n+1
        n=g
        print('%d'%n)
        
