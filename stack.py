class Stack(object):
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def display_stack(self):
        for i,val in enumerate(self.items):
            print(i,val)
#    def search_stack(self,item1):
#        for i in self.items:
#            if item1==i:
#                print("Element %d found! " %item1 )
#                break
#            else:
#                print("There is no such element in stack!")
s=Stack()
