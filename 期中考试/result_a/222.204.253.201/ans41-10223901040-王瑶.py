a=int(input("请输入行数："))
if a%2==0:
    a+=1
print("*"*a)
for i in range(1,a-1):
    print(" "*(a//2-1),"*"," "*(a//2-1))
print("*"*a)
