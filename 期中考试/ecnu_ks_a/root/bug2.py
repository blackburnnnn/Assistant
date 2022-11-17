ss=input("请输入字符串:")
while ss != 'stop':
    upper,lower,digit=0,0,0
    for x in range(ss):
        if x.isupper():
            upper=upper+1
        if x.islower():
            lower=lower+1
        if isdigit(x):
            digit=digit+1
        if upper>0 and lower>0 and digit>0:
            print('存在')
    ss=input("请输入字符串:")