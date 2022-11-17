for a in range(1,10):
    for b in range(1,a+1):
        c=a*b
        print(f"{a:<3.1f}*{b:3.1f}={c:3.1f}",end="")
        if b==a:
            print()
