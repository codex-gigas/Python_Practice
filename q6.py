import math as m
c=50
h=30
Q=[]
d=[i for i in input().split(',')]
for j in d:
	q=m.sqrt((2*c*float(j))/h)
	Q.append(str(round(q)))
print(','.join(Q))