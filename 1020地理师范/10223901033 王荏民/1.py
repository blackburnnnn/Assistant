count=0
for cock in range(51):
    for hen in range(34):
        chick=100-cock-hen
        if cock*2+hen*3+chick/3==100:
            print('可以买{}只公鸡,{}只母鸡,{}只小鸡'.format(cock,hen,chick))
        count+=1
print('共有%d种方法'%count)
