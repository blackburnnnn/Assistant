order=input('输入一串转向指令')
robot=E
E=int(E)
W=int(W)
N=int(N)
S=int(S)
R=int(R)
L=int(L)
B=int(B)
N+L=W
N+R=E
E+L=N
E+R=S
W+L=S
W+R=N
S+R=W
S+L=E
N+B=S
S+B=N
E+B=W
W+B=E
if order==L:
    robot+=L
    if order==R:
        robot+=R
    if order==B:
        robot+=B
        print('最后机器人面向：'.format(robot))
        
