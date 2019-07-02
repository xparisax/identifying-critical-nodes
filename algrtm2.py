import copy, math

# Reads the Graph from file
Vertices = int(input('enter Number of Vertices: '))
k_bound = int(input('enter k_bound or enter 0: '))
if k_bound == 0:
    k_bound = math.ceil(0.36 * Vertices)

# file_name = input("enter data file name (e: file_name.txt): ") 
my_file = list(open("graph_sample.txt", 'r')) # graph_sample.txt
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

# Representing Equation 1
def func(concom): 
    return concom*(concom - 1) / 2

# Removes vertex v from graph G
def remove_vertex(graph, v_star):
	nodes = graph[v_star]
	for u in nodes:
		graph[u].remove(v_star)
	graph[v_star] = []

# Appendix
def evaluate(v, visited, ap, parent, low, disc, time, subt_size, impact, cut_size):
    children = 0
    visited[v] = True
    disc[v] = time
    low[v] = time
    time += 1

    for u in graph[v]:
        if visited[u] == False:
            parent[u] = v
            children += 1
            subt_size[u] = 1
            impact[u] = 0
            evaluate(u, visited, ap, parent, low, disc, time, subt_size, impact, cut_size)
            # Check if the subtree rooted with u has a connection to 
            # one of the ancestors of v
            low[v] = min(low[v], low[u])
            # (1) v IS root of DFS tree and has two or more chilren.
            if parent[v] == -1 and children > 1:
                ap[v] = True
            #(2) If v IS NOT root and low value of one of its child is more 
            # than discovery value of v. 
            if parent[v] != -1 and low[u] >= disc[v]:
                ap[v] = True
                cut_size[v] += subt_size[u]
                impact[v] += func(subt_size[u])
        # Update low value of u for parent function calls 
        elif u != parent[v]:
            low[v] = min(low[v], disc[u])

# ap == articulation point
def art_point():
    removed = []
    visited = [False]*Vertices
    disc = [0]*Vertices
    low = [0]*Vertices
    cut_size = [0]*Vertices
    subt_size = [0]*Vertices
    impact = [0]*Vertices
    parent = [-1]*Vertices
    ap = [False]*Vertices
    time = 0

    for node in range(Vertices):
        if visited[node] == False:
            evaluate(node, visited, ap, parent, low, disc, time, subt_size, impact,cut_size)
    # Removes the APs
    for index, value in enumerate(ap):
        if len(removed) < k_bound and value == True:
            remove_vertex(graph, index)
            removed.append(index)
            
    for v, check in enumerate(visited):
        if check:
            if ap[v]:
                impact[v] += func(time - cut_size[v])
            else:
                impact[v] += func(time - 1)
    print(removed, ap)

art_point()
