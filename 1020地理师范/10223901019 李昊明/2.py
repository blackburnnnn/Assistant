for x in range(1,10):
    for y in range(1,x+1):
        z=x*y
        print('%.1f*%.1f=%.1f'%(x,y,z),end='\t')
    print('')
