import random

Vertices = int(input('Number of Vertices'))
k_bound = int(input('k_bound or enter 0'))
Removed = set()
if k_bound == 0:
    k_bound = int(0.036 * Vertices)

cmm_clique = int((Vertices*(Vertices-1) / 2) * random.random())
E = set()

for edge in range(cmm_clique): #is a number
    u = random.randint(0, Vertices)
    v = random.randint(0,Vertices)
    if u == v:
        continue
    E.add((u,v))

graph_input = open("graph_input.txt" ,'w')
for e in E:
    graph_input.write(str(e[0]) + ' ' + str(e[1]) + '\n')
graph_input.close()