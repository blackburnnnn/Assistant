num=int(input('请输入行数'))
if num%2!=0:
    for item in range(0,num):
        print(item)
else:
    num+=1
    for item in range(0,num):
        print(item)
