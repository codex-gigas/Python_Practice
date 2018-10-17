l=[]
k=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
for i in range(2000,3201):
	if (i%7==0) and (i%5!=0):
		l.append(str(i))
b=','.join(l)
print(type(b))
for j in k:
	print(','.join(j))
	