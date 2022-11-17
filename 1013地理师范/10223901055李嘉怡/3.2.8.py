n = int(input("n="))
result=[n]
while n!=1:
    if n%2==0:
        n=int(n/2)
        result.append(n)
    elif n==1:
        result.append(1)
        break
    else:
        n=int(3*n+1)
        result.append(n)
print(result)


