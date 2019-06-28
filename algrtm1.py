import copy, math

Vertices = int(input('enter Number of Vertices: '))
vertices = [True for i in range(Vertices)]
k_bound = int(input('enter k_bound or enter 0: '))
if k_bound == 0:
    k_bound = math.ceil(0.36 * Vertices)

file_name = input("enter data file name: ")
my_file = list(open(file_name, 'r'))
edge = []
for line in my_file:
	edge.append(line)
	edge = [x.strip() for x in edge]

graph = [ [] for i in range(Vertices) ]
edg_control = [] # Consists of edges only appeared once -> edges
for data in edge:
	u, v = data.split()
	u, v = int(u), int(v)
	if ( (u,v) in edg_control ) or ( (v,u) in edg_control ):
		continue
	graph[u].append(v)
	graph[v].append(u)
	edg_control.append((u,v))
	edg_control.append((v,u))

def objective_func(graph, Vertices): # The First Equation
	func = [0 for i in range(Vertices)] # Number of connected components of each v

	def dfs(v, visited, temp):
		visited.append(v)
		temp.append(v)
		for u in graph_copy[v]:
			if u not in visited:
				temp = dfs(u,visited, temp)
		return temp

	for v_star in range(Vertices):
		if vertices[v_star] == False:
			continue
		graph_copy = copy.deepcopy(graph)
		remove_vertex(graph_copy, v_star)
		visited = []
		cc = []
		temp = []
	
		for v in range(Vertices):
			if graph_copy[v] == []:
				continue # The deleted node
			if v not in visited:
				temp = []
				cc.append(dfs(v,visited, temp))
				func[v_star] +=1 

	check = Vertices
	node = 0
	for i in func:
		if i == 0:
			continue
		if i < check:
			v_star = node
		node += 1
 
	return v_star

def remove_vertex(graph, v_star):
	nodes = graph[v_star]
	for u in nodes:
		graph[u].remove(v_star)
	graph[v_star] = []
	

Removed = set()

while len(Removed) < k_bound: # Bound is guarateed 
	v_star = objective_func(graph, Vertices)
	remove_vertex(graph, v_star)
	vertices[v_star] = False
	Removed.add(v_star)
	
