def createEmptyList(n):
    L={}
    for i in range(n):
        L[i]=[]
    return L

f=open("graph.txt","r")
Vertex_Edge=f.readline()
V_E=Vertex_Edge.split(" ")
n=int(V_E[0])
m=int(V_E[1])
print(n,m)
graph=createEmptyList(n)

for i in range (m):
    line=f.readline()
    u_v=line.split(" ")
    u=int(u_v[0])
    v=int(u_v[1])
    graph[u].append(v)
    #graph[v].append(u)
print(graph)    
