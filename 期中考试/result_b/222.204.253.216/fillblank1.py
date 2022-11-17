#ans31-10223901036-宋琰芸
money = int(input("请输入消费金额："))
count=0            
for young in range(0,13):
for old in range(0,13-young):    
        child=12-young-old
        if child*100+young*300+old*200==money  
            count+=1
            print ("第{}种情况：".format(count))  
            print ("年轻人有{}人，老人有{}人，小孩有{}人。".format(young,old,child))
