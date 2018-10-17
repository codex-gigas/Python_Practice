class Node:
	def __init__(self,value):
		self.info=value
		self.link=None

class SingleLinkedList:
	def __init__(self):
		self.start = None

	def create_list(self):
		n = int(input("ENter the number of nodes : "))
		if n==0:
			return
		for i in range(n):
			data = int(input("Enter the elements : "))
			self.insert_end(data)


	def display_list(self):
		if self.start is None:
			print('List is empty')
			return
		else:
			print("List is : ")
			p=self.start
			while p is not None:
				print(p.info , ' ', end=' ')
				p=p.link
			print()

	def count_node(self):
		n=0
		p=self.start
		while p is not None:
			n+=1
			p=p.link
		print("Number of nodes in the list: ",n)

	def search(self,x):
		position=1
		p=self.start
		while p is not None:
			if p.info==x:
				print(x, " is at position ", position)
				return True
			position+=1
			p=p.link
		else:
			print(x," not found in list")
			return False

	def insert_begin(self,data):
		temp=Node(data)
		temp.link=self.start
		self.start=temp

	def insert_end(self,data):
		temp=Node(data)
		if self.start is None:
			self.start=temp
			return
		p=self.start
		while p.link is not None:
			p=p.link
		p.link=temp

	def insert_after(self,data,x):
		p=self.start
		while p is not None:
			if p.info == x:
				break
			p=p.link
		if p is None:
			print(x, "not present in the list")
		else:
			temp=Node(data)
			temp.link=p.link
			p.link=temp

	def insert_before(self,data,x):
		if self.start is None:
			print('List is empty')
			return
		if x==self.start.info:
			temp=Node(data)
			temp.link=self.start
			self.start=temp
			return
		p=self.start
		while p.link is not None:
			if p.link.info==x:
				break
			p=p.link

		if p.link is None:
			print(x, "not present in the list")
		else:
			temp=Node(data)
			temp.link=p.link
			p.link=temp

	def insert_position(self,data,k):
		if k==1:
			temp=Node(data)
			temp.link=self.start
			self.start=temp
			return
		p=self.start
		i=1
		while i<k-1 and p is not None:
			p=p.link
			i+=1
		if p is None:
			print('You can insert only upto position ', i)
		else:
			temp=Node(data)
			temp.link=p.link
			p.link=temp


	
l=SingleLinkedList()
print("1.create a list")
print("2.display_list")
print("3.search element in a list")
print("4.Insert at begin")
print("5.Insert at end")
print("6.")
print("1.create a list")
print("1.create a list")
ch=int(input("Enter your choice : "))
