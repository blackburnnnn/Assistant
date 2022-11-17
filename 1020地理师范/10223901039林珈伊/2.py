a=0
b=0
for i in range(0,9):
    a+=1
    for j in range(1,i+2):
        b=j
        s=a*b
        print(f'{a:1.1f}*{b:1.1f}={s:1.1f}',end=' ')
    print()
