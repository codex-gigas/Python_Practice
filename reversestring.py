inp=input("Enter a string: ")
rev=0
while (inp>0):
	dig=inp%10
	rev=rev*10+dig
	inp=inp//10
print(rev)