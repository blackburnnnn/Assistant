#老师，这个程序我不知道哪里错了，改好几遍了，
s=0
t=0
for i in range(3,1001):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        t+=1
        print(s)
print("1~1000间的完数有",t)
