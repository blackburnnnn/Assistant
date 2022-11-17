n=int(input('请输入行数:'))
if n//2!=0:
     n+=1
     count=0
     line=1
     while True:
          print('*',end='')
          count+=1
          if count==n:
               print('*',end='\n')
               line+=1
               if line==6:
                    print('*',end='')
                    count+=1
                    if count==n*2:
                         break
