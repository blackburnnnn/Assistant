for i in range(1,10):
    j=0
    while j<i:
        j+=1
        q=i*j
        print("%.1f*%.1f=%.1f"%(i,j,q),end=" ")
    print()
