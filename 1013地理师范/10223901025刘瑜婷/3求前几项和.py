#求分数序列前n项和
n=int(input("需求前几项和"))
if n<=0:
    print("n输入错误")
numA=1
numB=2
S=0
for i in range(n):
    S+=numB/numA
    numA,numB=numB,numA+numB
print("前几项和为",S)
    
