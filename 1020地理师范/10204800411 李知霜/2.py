i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i}*{j}={i*j}",end='\t')
        j = j+1
    print("")
    i = i+1
