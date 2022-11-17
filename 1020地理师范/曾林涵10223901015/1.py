for row in range(1,10):
    for col in range(1,row+1):
        print("{0}*{1}={2:2d}".format(row,col,row*col),end=" ")
    print(" ")
        
