def createEmptyList(n):
    L={}
    for i in range(n):
        L[i]=[]
    return L

f=open("graph.txt","r")
Vertex_Edge=f.readline()
V_E=Vertex_Edge.split(" ")
n=int(V_E[0]) #Number of vertex
m=int(V_E[1]) #Number of edges
print(n,m)
graph=createEmptyList(n)

for i in range (m):
    line=f.readline()
    u_v=line.split(" ")
    u=int(u_v[0])
    v=int(u_v[1])
    graph[u].append(v)   # Directed graph
    #graph[v].append(u)  # UNdirected graph

print(graph)    
