num=0
for a in range(1,4):
 for b in range(0,4):
  for c in range(0,4):
   if a!=b and a!=c and b!=c:
       l=a*100+b*10+c
       print(l)
       num+=1
print(f"共{num}")
