for x in range (1,34):
    for y in range (1,51):
        for z in range (1,300):
            if x+y+z==100 and 3*x+2*y+z/3==100:
                print(f'母鸡:{x}公鸡:{y}小鸡:{z}')
            
