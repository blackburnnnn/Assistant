Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=0
>>> for i in range(1,1000):
	list 1=[]
	
SyntaxError: invalid syntax
>>> list1=[]
>>> for j in range(1,i):
	if i%j==0:
		list1.append(j)
    if sum(list1)==i:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if sum(list1)==i:
	print(i)
	n+=1
	print('1~1000间的完数总共有',n,'个',sep="")

	
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    if sum(list1)==i:
NameError: name 'i' is not defined
>>> 