a=int(input("请输入行数:"))
if a%2!=0:
    a=a
else:
    a+=1
print("*"*a)
b=int((a-1)/2)
for i in range(0,a-2):
    print(" "*b+"*")
print("*"*a)
    
