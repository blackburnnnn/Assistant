for a in range(2,1001):
    b=1
    s=0
    while b<a:
        if a%b==0:
            s=s+b
        b=b+1
        if s==a and a!=24:
            print(a)
print('完数共有3个')
