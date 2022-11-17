n = int(input("n="))
for i in range (1,10000):
    if n%2 == 0:
        n=n/2
        print(n)
    else:
        n=3*n+1
        print(n)
    i=i+1
    while(n==1):
        quit()
