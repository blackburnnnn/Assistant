n=int(input("n="))
a=[]
while n!=1:
    if n % 2==0:
        n /=2
        a.append(int(n))
    elif n %2==1:
        n = n *3+1
        a.append(int(n))
print(a)
        


