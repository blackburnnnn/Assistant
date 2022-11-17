#sy3-8.py
n=int(input("n="))
while n!=1:
    if n%2==0:
        n/=2
        print('%.0f'%n,end="  ")
    else:
     n=3*n+1
     print('%.0f'%n,end="  ")
 
