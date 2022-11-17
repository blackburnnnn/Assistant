demand=input('输入一串转向指令')
countone,counttwo,countthree=0,0,0
for x in demand:
     if x=='L':
          countone+=1
     if x=='R':
          counttwo+=3
     if x=='B':
          countthree+=2
     count=countone+counttwo+countthree
     if count%4==1:
          a='N'
     elif count%4==0:
          a='E'
     elif count%4==2:
          a='W'
     else:
          a='S'
print('机器人最后面向:',a)
