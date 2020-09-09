import math
func = lambda x1,x2: math.sqrt(sum([(i-j)**2 for i,j in zip(x1,x2)]))
def calculate_cost(M,start,goal,expanded_nodes,current_cost=0):
    for m in M.roads[start]:
        #print(f'start = {start} {M.intersections[start]}')
        #print(f'm = {m} {M.intersections[m]}')
        #print(f'goal = {goal} {M.intersections[goal]}')
        g = current_cost+func(M.intersections[start],M.intersections[m])
        h = func(M.intersections[m],M.intersections[goal])
        f = g+h
        expanded_nodes += [(f,g,h,start,m)]
    print('before sorting')
    for r in expanded_nodes: print(r)
    expanded_nodes = sorted(expanded_nodes)
    print('sorted')
    for r in expanded_nodes: print(r)
    return expanded_nodes


def shortest_path(M,start,goal):
    print("shortest path called")
    print(start,goal)
    shortest_path=list()
    g=0
    h=func(M.intersections[start],M.intersections[goal])
    f=g+h
    expanded_nodes = [(f,g,h,start,start)]
    while len(expanded_nodes) > 0:
        node = expanded_nodes.pop(0)
        print(f'popped node: {node}')
        start = node[-1]
        shortest_path += [start]
        if start == goal:
            break
        current_cost = node[1]
        print(f'current_cost = {current_cost}')
        expanded_nodes = calculate_cost(M,start,goal,expanded_nodes,current_cost=current_cost)
        break
    print(shortest_path)
    return shortest_path