for i in range(0,4):
    for j in range(0,4):
        if j==i:
            continue
        for k in range(0,4):
            if k==i or k==j:
                continue
            print(i,j,k)
