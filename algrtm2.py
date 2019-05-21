from algrtm1 import *

q = 1 ###########     FUNCTION TO AKNOWLEDGE V* IN ALG3     ###########
p_que = []
deleted = []
visited = [] # where to check visited? in alg2 line 17 || alg3 ? 

p_que.append(q)
Removed = set()

while len(Removed) <= k_bound:
    v_star = p_que.pop() #always pop?
    remove_vertex(graph, v_star)
    Removed.add(v_star)
    deleted.append(v_star)

    for neighbor in graph[v_star]: # neighbor == b in paper
        if neighbor in visited:
            continue
        w = 1 #####################      # find w ∈ G, rooted at b using EVALUATE (vertex)      #############
        p_que.append(w)
