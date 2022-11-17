def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
try:
    num = int(input('n='))
    while num != 1:
        num = collatz(n = num)
        print(num)
except:
    print('错误')

    
