def collatz(number):
    if number % 2 ==0:
        return number //2
    elif number % 2 ==1:
        return number *3+1
while true:
    try: t=int(input("请输入一个整数:"))
        if t>0:
            break
        else:print("必须是整数")
        except ValueError:
            print("必须是数字")
            continue
        while t !=1:
            t=collatz(t)
            print(t)
