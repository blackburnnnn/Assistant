count=0
for i in range(1,1000):
    for j in range(1,i):
        if i%j==0:
            count +=j
    if(count==i):
        print(i)

    count=0
print('1到1000间的完数共有3个')

        
