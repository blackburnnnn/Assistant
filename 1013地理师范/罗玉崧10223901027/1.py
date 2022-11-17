m,s,x,y,w,f,h=2,2,2,1,1,0,1
n=int(input("n的值为"))
if n<=0:
    print("你丫是不是要搞我")
elif n==1:
    print("前1项和为2")
else:
    while x<=n:
        f=m+w
        h=h+y
        s=s+f/h
        m=f
        y=w
        w=h
        x=x+1
    print("前",n,"项和为",s)   
        
          
