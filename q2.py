def factorial(n):
	sum=1
	if n==0:
		return 1
	else:
		for i in range(1,n+1):
			sum=sum*i
	return(sum)

a=factorial(int(input('Enter a number: ')))
print(a)