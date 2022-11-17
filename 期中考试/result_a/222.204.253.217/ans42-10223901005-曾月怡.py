order=input("输入一串转向指令")
count=0
for i in order:
    if i=='R':
        count+=1
    if i=='L':
        count+=-1
    if i=='B':
        count+=2
if count%4==0:
    print('最后机器人面向：E')
if count%4!=0 and count%2==0:
          print('最后机器人面向：W')
if count<0 and count%3!=0:
                print('最后机器人面向：N')
if count>0 and count%3==0:
          print('最后机器人面向：N')
if count>0 and count%3!=0:
           print('最后机器人面向：S')
if count<0 and count%3==0:
          print('最后机器人面向：S')
          
          
