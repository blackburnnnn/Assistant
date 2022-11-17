x=input("请输入一个气温：")
if x=="quit":
        print("程序结束")
        exit(0)
else:
        maxnum=minnum=x
        
s=0
n=0

while True:
        x=input("请输入一个气温：")
        if x=="quit":
                continue
        x=int(x)
        if x>maxnum:
                maxnum=x
        elif x<minnum:
                minnum=x
        s=s+x
        n=n+1
        print("最高气温为：{},最低气温为：{}".format(maxnum,minnum))
        print("平均气温为：{:.1f} ".format(s/n))
