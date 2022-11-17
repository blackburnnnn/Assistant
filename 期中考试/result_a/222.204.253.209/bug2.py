#王荏民10223901033.py
ss=input("请输入字符串:")
while ss != 'stop':  
    upper,lower,digit=0,0,0 
    if x.isupper():   
            upper=upper+1
    elif x.lower():
            lower=lower+1
    elif x.isdigit():
            digit=digit+1
    elif upper>0 and lower>0 and digit>0: 
            print('存在')     
    ss=input("请输入字符串:")  
