#有四个数字，0、1、2、3，能组成多少个互不相同且无重复数字的三位数？各是多少？每行输出10个。
num=0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if(i!=j)&(i!=k)&(j!=k):
                print(i*100+j*10+k,end=" ")
                num+=1
                if num%10==0:
                    print(end="\n")
print("\n共%d个"%num)
