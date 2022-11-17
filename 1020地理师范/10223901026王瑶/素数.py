# 10223901026 王瑶 有多余空行

count=0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print('{:>3d}'.format(i),end='')
        count=count+1
    if count%5==0:
        print()
       
