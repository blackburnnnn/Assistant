x=int(input("请输入行数："))
if x%2==1:
    s=x
elif x%3==0:
    s=x+1
q=''
for i in range(s):
    q+='*'
print(q)
for i in range(s-2):
    print('   *',)
print(q)
