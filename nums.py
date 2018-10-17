l=[0]
for i in range(1,16):
	if i%3==0:
		if i%5==0:
			l.append("THREEFIVE")
		else:
			l.append("THREE")
	elif i%5==0:
		l.append("FIVE")
	else:
		l.append(i)
print(l)
