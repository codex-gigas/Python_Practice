def average():
	sum=0
	n=[i for i in map(int,input().split(','))]
	for i in n:
		sum=sum+i
	avg=sum/len(n)
	print(avg)

average()