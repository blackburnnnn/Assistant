x=int(input('请输入行数:'))
i='*'
if x%2!=0:
   n=int((x-1)/2)
   e=i*x
   j=' '*n+'*'+' '*n
   print(e)
   for w in range(0,x-1):
        print(j)
   print(e)
else:
    x=x+1
    n=(x-1)/2
    e=i*x
    j=' '*n+'*'+' '*n
    print(e)
    for w in range(0,x-2):
        print(j)
    print(e)   
