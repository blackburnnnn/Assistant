for i in range(1,1001):
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=j
    if count==i:
        print(i)
print("1-1000间的完数共有3个")
