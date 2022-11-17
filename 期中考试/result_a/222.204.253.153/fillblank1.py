#fillblank1.py
money = int(input("请输入消费金额："))
count=young*300+old*100+child*100            #count统计组合数
for young in range(0,13):
    for old in range(0,13):    
        child=12-young-old
        if child<0:   
            count+=1
            print ("第{}种情况：".format(count),young*300+old*100+child*100)  
            print ("年轻人有{}人，老人有{}人，小孩有{}人。")
