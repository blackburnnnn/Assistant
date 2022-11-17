money = int(input("请输入消费金额："))
count=0            #3分
for young in range(0,13):
    for old in range(0,13-young):   #3分
        child=12-young-old
        if young*300+old*200+child*100==money:   #3分
            count+=1
            print ("第{}种情况：".format(count),end=" ")  #
            print ("年轻人有{}人，老人有{}人，小孩有{}人。".format(young,old,child))
