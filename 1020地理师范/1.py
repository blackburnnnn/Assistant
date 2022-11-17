price_hen=3
price_rooster=2
price_chick=1/3
for num_hen in range(1,98):
    for num_rooster in range(1,98):
        for num_chick in range(1,98):
            num_hen=100-num_rooster-num_chick
            if price_hen*num_hen+price_rooster*num_rooster+price_chick*num_chick==100 and num_hen>=1 and num_rooster>=1 and num_chick>=1:

                print("母鸡只数",num_hen)
                print("公鸡只数",num_rooster)
                print("小鸡只数",num_chick)