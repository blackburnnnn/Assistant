for i in range(1,10):
    for j in range(1,i+1):
        if i>=j:
            print("{}*{}={}".format(float(i),float(j),float(i*j)),end=" ")
    else:
        print("\n")
