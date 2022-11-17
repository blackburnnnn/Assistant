for x in range(1,33):
    for y in range(1,50):
        z=100-x-y
        if 3*x+2*y+1/3*z==100 and z%3==0:
            print('muji=',x,'gongji=',y,'xiaoji=',z)
