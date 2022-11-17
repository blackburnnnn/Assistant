n=int(input('n='))
while n!=1:
    if n%2==0:
        k=int(n/2)
        n=k
        print('%d'%n)
    elif n==1:
        print('%d'%n)
        break
    else:
        g=int(3*n+1)
        n=g
        print('%d'%n)
