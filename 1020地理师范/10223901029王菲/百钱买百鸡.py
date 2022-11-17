for male in range(1,34):
    for female in range(1,50):
        chicken=100-male-female
        if male*3+female*2+chicken/3==100:
            print(f'母鸡买{male}只，公鸡买{female}只，小鸡买{chicken}只。')
            
