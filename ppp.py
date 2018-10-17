inp=str(input('enter string'))
for i in inp:
	if i!=None:
		inp=inp+'\b'
		print(inp)