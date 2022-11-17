# 10223901005 曾月怡
# 输出错误
count=0
for m in range (2,100):
    for n in range (2,100):
        if m%n==0:
            break
        else:
            if count%5==0:
                print(m,' ')
                count+=1
            else:
                if m<10:
                    print('',m,'',end='')
                    count+=1
                else:
                    print(m,'',end='')
                    count+=1

         
    
   
        
    
        
            

        
