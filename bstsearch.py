class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.value=key
def insert(root,node):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right is None:
				root.right=node
			else:
				inset(root.right,node)
		else:
			if root.left is None:
				root.left=node
			else:
				insert(root.left,node)

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)




def Search(root,key):
	if root==None or root.val==key:
		return root
	if root.val<key:
		return Search(root.right,key)
	return Search(root.left,key)

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

print(Search(60))
