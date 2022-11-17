direction=input("输入一串转向指令")
ans=['E','N','W','S']
n=0
for i in direction:
    if i=='L':
        n=n+1
    if i=='R':
        n=n-1
    else:
        n=n+2
while n>3:
    n=n-4
print("最后机器人面向："+ans[n])
   
