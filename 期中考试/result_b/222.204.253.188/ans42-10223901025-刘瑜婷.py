a=input()
j=90
if a=='':
    print("E")
for x in a:
    if x=='L':
        j=j-90
    if x=='R':
        j=j+90
    if x=='B':
        j=j+180
if j%360==0:
    print("N")
else:
    j=j%360
    if j==90:
        print("E")
    if j==180:
        print("S")
    if j==270:
        print("W")

        
