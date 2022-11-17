n=input('输入一串转向指令:')
if n[-1]=='L':
    print('最后机器人面向:S')
if n[-1]=='R':
    print('最后机器人面向:N')
if n[-1]=='B':
    print('最后机器人面向:W')
if n[-1]=='':
    print('机器人保持原朝向')
