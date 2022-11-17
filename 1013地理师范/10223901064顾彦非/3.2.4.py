num = 0
for n in range(1,1000):
    sum = 0
    i = 1
    while  i <= n-1 :
        if n % i == 0: 
            sum += i
        i = i + 1
    if sum == n :
        print(n)
        num+=1
    else:
        num+=0
print('前一千个数中有',num,'个完数')
