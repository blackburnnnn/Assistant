x=int(input("请输入行数："))
if x%2!=0:
    x=x
else:
    x+=1
print("*"*x)
y=int((x-1)/2)
for i in range(0,x-2):
    print(""*y+"*")
print("*"*x)
    
