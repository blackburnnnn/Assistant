﻿#fillblank1.py
monemoney=int(input("请输入消费金额："))
councount=0            #count统计组合数
for young in range(0,13):
    for old in range(0,12-young):    
        child=12-young-old
        if  money==300*young+200*old+100*child:   
            count+=1
            print ("第{}种情况：".format(count),'/t')  
            print ("年轻人有{}人，老人有{}人，小孩有{}人。".format(young,old,child))
