ss=input("输入一串转向指令：")
t=0
for x in ss:
    if x=="L":
        t=t+1
    if x=="R":
        t=t-1
if t-(t//4)*4==0:
    print("最后机器人面向:E")
if t-(t//4)*4==1:
    print("最后机器人面向:N")
if t-(t//4)*4==2:
    print("最后机器人面向:W")
if t-(t//4)*4==3:
    print("最后机器人面向:S")
