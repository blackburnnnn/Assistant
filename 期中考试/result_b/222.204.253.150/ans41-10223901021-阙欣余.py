a=int(input('请输入行数：'))
i=1
b=str('*')
if a%2==1:
    b=b*a
    print(b)
    while i<a-1:
        print('   *')
        i=i+1
    print(b)
if a%2==0:
    b=b*(a+1)
    print(b)
    while i<a:
        print('*')
        i=i+1
    print(b)
