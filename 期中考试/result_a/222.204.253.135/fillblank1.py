#fillblank1.py
money=int(input("请输入消费金额："))
councount=0            #count统计组合数
for for young in range(0,13):
      for old in range(0,13):
          child=12-young-old
          if young>0 and old>0 and child>0 and 300*young+200*old+child*100==y:   
            count+=1
            print ("第{}种情况：".format(count),end=' ')  
            print ("年轻人有{}人，老人有{}人，小孩有{}人。".format(young,old,child))
