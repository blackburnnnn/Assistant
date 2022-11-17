while True:
   n=int(input("请输入n的值:"))
   try:
      n>0
      a=2
      b=1
      s=0
      for i in range(n):
           c=a
           a=a+b
           b=c
           s += a/b
      print("前{:d}项的累加和为{:4.2f}".format(n,s))
      break
   except:
     print("n输入错误")
