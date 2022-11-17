E,N,W,S=0,1,2,3
x=0
i=print("输入一串转向指令")
if i==int(L):
      x=x+1
if i==int(R):
      x=x+3
if i==int(B):
      x=x+2
   if x%4==0:
       print('最后机器人面向：E')
   if x%4==1:
       print('最后机器人面向：N')
   if x%4==2:
       print('最后机器人面向：W')
   if x%4==3:
       print('最后机器人面向：S')
