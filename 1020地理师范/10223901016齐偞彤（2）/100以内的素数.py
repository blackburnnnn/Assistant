count=0
for a in range(2,101):
    for b in range(2,a):
        if a%b==0:
            break
    else:
        count+=1
        if count%5==0:
            print('{:>2}'.format(a))
        else:
            print('{:>2}'.format(a),end='\t')
