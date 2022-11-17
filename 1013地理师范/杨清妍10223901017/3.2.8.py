n=int(input("n="))
while n%2==0:
      m=n/2
      n=m
      print(int(n),end='\t')
      if n==1:
            break
      while n%2!=0:
          n=3*n+1
          print(int(n),end='\t')
          if n==1:
                  break
else :
      n=3*n+1
      while n%2==0:
            m=n/2
            n=m
            print(int(n),end='\t')
            if n==1:
                  break
            while n%2!=0:
                  n=3*n+1
                  print(int(n),end='\t')
                  if n==1:
                        break
     
