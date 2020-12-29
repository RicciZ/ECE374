class Edge:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w

def BellmanFord(E,V,source):
    d = [float('inf')]*len(V)
    d[source] = 0
    for _ in range(len(V)-1):
        for e in E:
            if d[e.v] > d[e.u] + e.w:
                d[e.v] = d[e.u] + e.w
    for e in E:
        if d[e.v] > d[e.u] + e.w:
            print("negative weight cycle detected")
            return -1
    return d

def ModifiedBellmanFord(E,V,source):
    d = [float('inf')]*len(V)
    d[source] = 0
    for _ in range(len(V)-1):
        for e in E:
            if d[e.v] > d[e.u] + e.w:
                d[e.v] = d[e.u] + e.w
    for _ in range(len(V)-1):
        for e in E:
            if d[e.v] > d[e.u] + e.w:
                d[e.v] = -float('inf')
    return d

graph = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,1),(4,3,-3)]
E = []
V = []
for i in graph:
    E.append(Edge(i[0],i[1],i[2]))
V = [i for i in range(5)]
for i in V:
    print(f"if vertex {i} is the source")
    d = BellmanFord(E,V,i)
    if d != -1:
        print(f"the shortest distance from source for each vertex is")
        print(d)
    print()

print()
print("for another graph with negative weight cycle")
graph = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,-1),(4,3,-3)]
E = []
V = []
for i in graph:
    E.append(Edge(i[0],i[1],i[2]))
V = [i for i in range(5)]
for i in V:
    print(f"if vertex {i} is the source")
    d = ModifiedBellmanFord(E,V,i)
    if d != -1:
        print(f"the shortest distance from source for each vertex is")
        print(d)
    print()