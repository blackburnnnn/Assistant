x=int(input("请输入行数:"))
if x//2==0:
             x=x+1
for i in range(0,x):
             print("*",end='')
print('\n')
for i in range(0,x-2):
             print(" "*(x//2),end='')
             print('*')
             print(" "*(x//2),end='\n')

for i in range(0,x):
             print("*",end='')
                 
             
