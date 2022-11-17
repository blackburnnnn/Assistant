s= int(input("请输入行数："))
if s%2==1:
    for i in range(0,s):
        print('*******')
else:
    s=s+1
    for i in range(0,s):
        print('*******')
