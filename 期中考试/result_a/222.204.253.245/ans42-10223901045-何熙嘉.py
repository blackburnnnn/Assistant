x=input('输入一串指令')
l=len(x)
y=''
if x[0]=='L':
   y='N'
elif x[0]=='R':
   y='S'
elif x[0]=='B':
   y='W'
elif x[0]==' ':
   y='E'
for i in range(1,l):
   if y=='N':
      if x[i]=='L':
         y='W'
      elif x[i]=='R':
         y='E'
      elif x[i]=='B':
         y='S'
      elif x[i]==' ':
         y='N'
   elif y=='S':
       if x[i]=='L':
         y='E'
       elif x[i]=='R':
         y='W'
       elif x[i]=='B':
         y='N'
       elif x[i]==' ':
         y='S'
   elif y=='W':
       if x[i]=='L':
         y='S'
       elif x[i]=='R':
         y='N'
       elif x[i]=='B':
         y='E'
       elif x[i]==' ':
         y='W'
   elif y=='E':
       if x[i]=='L':
         y='N'
       elif x[i]=='R':
         y='S'
       elif x[i]=='B':
         y='W'
       elif x[i]==' ':
         y='E'
print('最后机器人面向：{}'.format(y))        
      

