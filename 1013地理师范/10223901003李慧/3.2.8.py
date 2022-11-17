n=int(input("n="))
if n==1:
 print(1)
else:
    while n!=1:
     if n%2==0:
        n=n/2
        print(n,end=" ")
     elif n%2==1:
      n=3*n+1
      print(n,end=" ")
