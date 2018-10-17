str1=str(input())
data=str1.split('#')
a=[]
p=[]
for i in range(len(data)):
	d=data[i].split('@')
	a.append(d)
for j in a:
	for k in j:
		if k=='-1':
			continue
		else:
			p.append(int(k))
print(p)