#ans22答案.py
ss=input("请输入字符串:")
while ss != 'stop':      
    upper,lower,digit=0,0,0    
    for x in ss:        # ss
        if x.isupper():   
            upper=upper+1
        if x.islower():
            lower=lower+1
        if x.isdigit(): # x.isdigit()
            digit=digit+1
    if upper>0 and lower>0 and digit>0: # 缩进
        print('存在')     
    ss=input("请输入字符串:") 
