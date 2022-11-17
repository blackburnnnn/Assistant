for i in range(1, 10):
    for j in range(1, i+1):
        print('{:0.1f}*{:0.1f}={:0.1f}'.format(j, i, i*j), end=' ')
    print()
