directions= 'ENWS'   #['E','N','W','S']
nowD=0#此时机器人的朝向
instruct=input('输入一串转向指令')#读入一串转向指令
for i in instruct:
    if i=='L':
       nowD=nowD+1
    elif i=='R':
        nowD=nowD+3
    else:
        nowD=nowD+2        
print('最后机器人面向：',directions[nowD%4])

