from networkx.algorithms.wiener import wiener_index
import networkx as nx
import matplotlib.pyplot as plt
def stringvalue(n):
    if (n < 10):
        value = "1"
        for i in range(2, n + 1):
            value = value + str(i)
        return value

def generatemoves(n):
    for i in range(1, n):
        for j in range(i, n + 1):
            for k in range(j + 1, n + 1):
                t = "0" + str(i) + str(j) + str(k)
                moves.append([0,i,j,k])

def generatePermutations(value, start, end, permute):
    current = 0
    if (start == end - 1):
        permute.append(value)
        return permute
    else:
        for current in range(start, end):
            x = list(value)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

            generatePermutations("".join(x), start + 1, end, permute)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

def graph_func(per,depth):
    temp=per
    maxdepth=(n//2)+1
    for move in moves:
        res = applymoves(temp, move)
        tmpres = res
        d = depth
        d = d + 1
        if d <= maxdepth:
            graph_func(tmpres, d)
    depth = 1

def applymoves(per,move):
    block1=""
    block2=""
    temp = per
    block1=temp[int(move[0]):int(move[1])]
    block2=temp[int(move[2]):int(move[3])]
    temp = temp.replace(block1, block2)
    length=len(temp)
    var=temp[0]
    temp=temp[1:length]
    temp=temp.replace(block2,block1)
    temp=var+temp
    G.add_edge(per,temp)
    return temp

def addnodes():
  for per in permute:
    G.add_node(per)

G = nx.Graph()
n = int(input("Enter a number: "))
moves = []
value = stringvalue(n)
permute=[]
addnodes()
generatemoves(n)
generatePermutations(value, 0, n, permute)
graph_func(value,1)
e_list = G.edges()
G = nx.Graph()
G.add_edges_from(e_list)
plt.figure(figsize =(15, 15))
nx.draw_networkx(G,node_color='yellow', node_size=5000, width=1,arrowstyle='-|>')
file1 = open("outputfile.txt","w")
file1.truncate(0)
file1.write("Permutation\t\t\tMoves")
file1.write("\n")
for i in permute:
  find=nx.shortest_path_length(G,i,value)
  k=str(i)+"\t\t\t\t\t\t\t"+str(find)
  file1.write(k)
  file1.write("\n")
