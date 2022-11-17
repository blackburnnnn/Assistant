for cock in range(1,100):
    for hen in range(1,100):
        for chick in range(1,100):
            if cock+hen+chick==100 and\
               2*cock+3*hen+chick/3==100:
                print("cock:{},hen:{},chick:{}"\
                      .format(cock,hen,chick))
