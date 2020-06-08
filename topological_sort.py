class Node:
    def __init__(self,name,color="white",successors=[]):
        self.name=name
        self.color=color
        self.successors=successors
        self.predecessors=[]
        self.discover=0
        self.finish=0        

def DFS(G):
    global time
    for vertex in G:
        vertex.predecessors=[]
    time=0
    for vertex in G:
        if vertex.color=="white":
            visit(G,vertex)

def visit(G,u):
    global time
    time+=1
    u.discover=time
    u.color="red"
    for v in u.successors:
        v.predecessors.append(u)
        if v.color=="white":
            #v.predecessors.append(u)#
            visit(G,v)
    u.color="blue"
    time+=1
    u.finish=time


def top_order(G):
    DFS(G)
    finishing_times=[(vertex.__dict__.get('name'),vertex.__dict__.get('finish'))for vertex in G]
    temp=sorted(finishing_times,key=lambda x: x[1],reverse=True)
    G2=[temp[i][0]for i in range(len(temp))]
    for vertex in G:
        for v in vertex.successors:
            if v in vertex.predecessors:
                return 'No topological order exists'
    return G2
    



"""
u=Node('u')
v=Node('v')
w=Node('w')
x=Node('x')
y=Node('y')
z=Node('z')
u.successors=[v,x]
v.successors=[y]
w.successors=[y,z]
x.successors=[v]
y.successors=[x]
z.successors=[z]
G=[u,v,w,x,y,z]
"""


A=Node('undershorts')
B=Node('pants')
C=Node('socks')
D=Node('shoes')
E=Node('watch')
F=Node('shirt')
G=Node('belt')
H=Node('tie')
I=Node('jacket')
A.successors=[B,D,G,I]
B.successors=[D,G,I]
C.successors=[D]
D.successors=[]
E.successors=[]
F.successors=[G,H,I]
G.successors=[I]
H.successors=[I]
I.successors=[]
Graph=[A,B,C,D,E,F,G,H,I]

"""
A=Node('a')
B=Node('b')
C=Node('c')
D=Node('d')
A.successors=[B,C]
B.successors=[C]
C.successors=[]
D.successors=[A,C]
G=[D,A,C,B]

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.successors=[b,c,d]
b.successors=[c,d]
c.successors=[b,d]
d.successors=[]
G=[a,b,c,d]


q=Node(1)
r=Node(2)
s=Node(3)
t=Node(4)
u=Node(5)
v=Node(6)
w=Node(7)
x=Node(8)
y=Node(9)
z=Node(10)
q.successors=[s,v,w,t,x,z,y]
r.successors=[u,y,q,s,v,w,t,x,z]
s.successors=[v,w]
t.successors=[y,x,z,q,s,v,w]
u.successors=[y,q,s,v,w,t,x,z]
v.successors=[w,s]
w.successors=[s,v]
x.successors=[z]
y.successors=[q,s,v,w,t,x,z]
z.successors=[x]
G=[q,r,s,t,u,v,w,x,y,z]
"""
