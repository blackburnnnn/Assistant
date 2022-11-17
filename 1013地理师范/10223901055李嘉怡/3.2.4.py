for n in range(1,101):
    s=0
    for i in range(1,int(n/2)+1):
        if n/i == int(n/i):
            s=s+i
    if s == n:
        print(n)
