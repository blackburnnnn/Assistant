#fillblank1.py
money = int(input("请输入消费金额："))
count=(young,old,child)           #count统计组合数
for young in range(0,13):
    for old in range(0,13-young):    
        child=12-young-old
        if young*300+old*200+child*100=2800:   
            count+=1
            print ("第{}种情况：".format(count){.:%})  
            print ("年轻人有{}人，老人有{}人，小孩有{}人。"{.:%})
