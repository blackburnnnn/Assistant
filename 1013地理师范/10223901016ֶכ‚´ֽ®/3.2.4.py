count=0
for i in range(1,1001,1):
    s=0
    for t in range(1,i,1):
        if i%t==0:
            s+=t
    if s==i:
        print(i)
        count+=1
print(f'1～1000间的完数共有{count}个')

