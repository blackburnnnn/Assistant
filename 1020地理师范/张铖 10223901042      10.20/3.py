count=1
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if count%5==0:
            print(i,'')
            count+=1
        else:
            if i<10:
                print('',i,'',end='')
                count+=1
            else:
                print(i,'',end='')
                count+=1
    
        
        
   
       
        
           
