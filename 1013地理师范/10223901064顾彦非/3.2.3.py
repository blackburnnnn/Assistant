n=int(input('请输入一个整数:'))
if n <= 0:
    print('n输入错误')
else:
    def g(n):
      if n <= 2:
        return n
      else:
        return g(n-1) + g(n-2)
    sum = 0
    for i in range(1,n+1):
      sum += g(i+1)/g(i)
    print('前',n,'位的和为',"%.2f" % sum)
