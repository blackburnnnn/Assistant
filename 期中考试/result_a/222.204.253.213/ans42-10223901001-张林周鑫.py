x=input('输入一串转向指令')
Direction="ENWS"
i=1
for d in x:
    if d=="L":
        i=i+1
    if d=="R":
        i=i-1
    if d=="B":
        i=i+2
while i<0:
    i=i+4
k=(i-1)%4+1
df=Direction[k-1]
print(f"机器人最后面向：{df}")
