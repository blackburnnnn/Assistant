n=int(input("请输入n的值"))
if n>0:
       a=1
       b=2
       s=0
       i=1
       for i in range (n) :
           s+=b/a
           c=b
           b+=a
           a=c
       print("前%d项的累加项为%4.2f"%(n,s))
else:
      print("n输入错误")
       
