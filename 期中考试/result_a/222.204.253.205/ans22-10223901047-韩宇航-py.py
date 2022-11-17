#10223901047 韩宇航
ss=input("请输入字符串:")
while ss != 'stop':  
    upper,lower,digit=0,0,0
    q=len(ss)
    x=ss
    for i in range(q):
        if x.isupper():   
            upper=upper+1
        elif x.islower():
            lower=lower+1
        elif x.isdigit():
            digit=digit+1
    if upper>0 and lower>0 and digit>0:
        print('存在')
        break
    ss=input("请输入字符串:")  
