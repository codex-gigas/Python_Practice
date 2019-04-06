def start():
	global maze
	maze=[[0 for i in range(12)] for j in range(12)]
	for i in range(12):
		maze[i][0]=-1
		maze[i][11]=-1
	for i in range(12):
		maze[0][i]=-1
		maze[11][i]=-1

def neighbours(i,j):
	return([(i-1,j),(i,j+1),(i+1,j),(i,j-1)])

def find(i,j):
	global maze,stack
	n=neighbours(i,j)
	for a,b in n:
		if maze[a][b]=='G':
			stack.append((a,b))
			return True
		if maze[a][b]==0:
			stack.append((a,b))
			maze[a][b]='Visited'
			extend=find(a,b)
			if extend:
				return True
			else:
				stack.pop()
				maze[a][b]="R"
	else:
		return False
	return True

def path():
	global stack,maze
	x,y=stack.pop()
	for i in range(len(stack)-1):
		x,y=stack.pop()
		maze[x][y]="P"

def print_Maze():
	global maze
	for i in range(1,11):
		for j in range(1,11):
			print(maze[i][j],end=" ")
		print("\n")

def Obstacles():
	global maze
	list1=[(1,2),(1,3),(1,4),(1,8),(2,2),(2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,2),(4,4),(4,6),(4,7),(4,8),(4,9),(5,2),(5,4),(5,6),(5,8),(6,2),(6,3),(6,4),(6,6),(6,8),(6,10),(7,2),(7,6),(7,8),(7,10),(8,2),(8,4),(8,5),(8,6),(8,8),(9,8),(10,5),(10,6),(10,7),(10,8)]
	for i,j in list1:
		maze[i][j]="B"

maze=[]
start()
sr,sc=0,0
stack=[(sr+1,sc+1)]
maze[sr+1][sc+1]="S"
gr,gc=9,9
maze[gr+1][gc+1]="G"
Obstacles()
find(sr+1,sc+1)
path()
print_Maze()
print("S=Start,P=Path,B=Blocked,R=Rejected,G=Goal,0=Notvisited")