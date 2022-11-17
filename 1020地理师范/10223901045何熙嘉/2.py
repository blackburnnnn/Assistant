for a in range(1,10):
    for b in range(1,a+1):
        a=float(a)
        b=float(b)
        c=a*b
        print(f'{a}*{b}={c} ',end='')
        if a==b:
            print()

