for i in range(1,100):
    sum = 0
    for k in range(1,i):
        if i % k == 0:
            sum = sum + k
        if sum == i:
            print(i)
            break
