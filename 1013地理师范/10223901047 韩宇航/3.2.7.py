total = 0
for i in range(1, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            if i != j and j != k and i != k:
                print(str(i)+str(j)+str(k), end=' ')
                total += 1
print(f"\n共有{total}个数")
