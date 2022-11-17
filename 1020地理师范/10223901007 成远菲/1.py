num=100
money=100
for hen in range(1,101):
    for cock in range(1,101):
        for chick in range(1,101):
            if hen+cock+chick==num and 3*hen+2*cock+(1/3)*chick==money:
                print('母鸡',hen,'公鸡',cock,'小鸡',chick)
