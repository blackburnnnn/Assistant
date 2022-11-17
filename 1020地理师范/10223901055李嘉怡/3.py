from math import sqrt
j = 2
nums = []
while j <= 100:
    i = 2
    k = sqrt(j)
    while i <= k:
        if j%i == 0:
            break
        i += 1
    if i > k:
        nums.append(j)
    j += 1
count = 0
for num in nums:
    print(num,end = " ")
    count += 1
    if count % 5 == 0:
        print(end = "  \n")
