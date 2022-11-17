n=int(input("请输入行数："))
if n%2 == 0:
    n=n+1
else:
    n=n
for i in range(1,n+1):
    print("*",end="")
print()
for i in range(1,n-1):
    print("*")
    print()
for i in range(1,n+1):
    print("*",end="")
    
