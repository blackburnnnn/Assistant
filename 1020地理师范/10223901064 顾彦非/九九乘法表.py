for j in range(1, 10):
    for i in range(1,j+1):
        k=i*j
        print("%.1f"%i,'*',"%.1f"%j,'=',"%.1f"%k,' ',end='')
    print()
