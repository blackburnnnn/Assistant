s=input('输入一串转向指令:')
robot=0
while True:
    for i in range(len(s)):
        x=s[i]
        if x=='L':
            robot+=1
        elif x=='R':
            robot-=1
        elif x=='B':
            robot+=2
        elif x==' ':
            robot=robot
    if robot%4==0:
        robot='E'
    elif robot%4==1:
        robot='N'
    elif robot%4==2:
        robot='W'
    elif robot%4==3:
        robot='S'
print('最后机器人面向：{}'.format(robot))
