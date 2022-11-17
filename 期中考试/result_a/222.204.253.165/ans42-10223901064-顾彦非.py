str=input('输入一串转向指令')
count=0
if str=='':
    print('最后机器人面向：E')
else:
    for x in str:
        if x=='L':
            count+=-1
        elif x=='R':
            count+=1
        else:
            count+=2
    if count<0:
        count=-count
        if count%4==1:
            print('最后机器人面向：N')
        elif count%4==2:
            print('最后机器人面向：W')
        elif count%4==3:
            print('最后机器人面向：S')
        else:
            print('最后机器人面向：E')
    elif count==0:
        print('最后机器人面向：E')
    else:
        if count%4==1:
            print('最后机器人面向：S')
        elif count%4==2:
            print('最后机器人面向：W')
        elif count%4==3:
            print('最后机器人面向：N')
        else:
            print('最后机器人面向：E')
        
