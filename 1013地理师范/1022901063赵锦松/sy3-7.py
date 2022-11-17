for i in range(100,400):
    a=i%10
    b=i%100%10
    c=i//100
    if a<4 and b<4 and a!=b and a!=c and b!=c:
        print(i)
print(i)
