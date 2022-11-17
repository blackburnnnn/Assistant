n=int(input("n="))
S=0
m=1
l=2
if n <= 0: 
    print("n输入错误") 
else:
    for i in range(n):
        S += l/m
        l,m = m+l,l  
    print("前五项的累加和为",S)
    
