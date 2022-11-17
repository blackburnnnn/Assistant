def collatz(number):
    if number%2==0:
       return number//2
    elif number%2==1:
       return number*3+1

t=int(input('n='))
while t!=1:
    t=collatz(t)
    print(t)
