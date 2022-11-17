x=int(input('请输入行数：'))
if x%2==0:
    x=x+1
while x%2!=0:
    print('*'*x)
    for i in range(x+1):
                a=int((x-1)/2)-1
                print(' '*a,'*',)
    print('*'*x)
    break
