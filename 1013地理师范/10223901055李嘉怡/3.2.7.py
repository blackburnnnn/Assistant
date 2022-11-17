def main():
    list1 = ['0','1','2','3']
    s = ''
    i = 1
    num = 0
    while(i < len(list1)):
        s = list1[i]
        j = 0
        while(j < len(list1)):
            if j == i:
                j += 1
                continue
            s = s[0:1]+list1[j]
            k = 0
            while(k < 4):
                if k == j or k == i:
                    k += 1
                    continue
                s = s[0:2] + list1[k]
                print(s,end="  ")
                num += 1
                if num%10 == 0:
                    print()
                k += 1
            j += 1
        i += 1

main()
                
    
