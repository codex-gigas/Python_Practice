class Input_data():
	def __init__(self):
		self.s=''
	def getString(self):
		self.s = input()
	def printString(self):
		print(self.s.upper())
strobj=Input_data()
strobj.getString()
strobj.printString()