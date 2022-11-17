j=1
for a in range (2,101):
    for i in range (2,a):
        if a%i==0:
          break
    else:
        if j%5==0:
            print(a,' ')
            j=j+1
        else:
            if a<10:
                print('',a,' ',end='')
                j=j+1
            else:
               print(a,' ',end="")
               j=j+1
    
