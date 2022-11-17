for b in range(1,10):
    for a in range(1,10):
        if a<=b:
            print("{:.1f}*{:.1f}={:.1f}".format(a,b,a*b),end='\t')
    print()
