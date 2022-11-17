n=int(input())
i=1
sum=p=2/1
while i<n:
    p=(1+p)/p
    sum=p+sum
    i=i+1
else:
    print(sum)
