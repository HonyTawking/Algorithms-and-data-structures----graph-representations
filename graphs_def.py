# n = int(input())  #vertex
# m = int(input()) #arcs
# d = m/n*n #density

def Adjacency_Matrix(n):
    matrix = []
    for i in range(n):
        a = [0]*n
        matrix.append(a)
    return matrix

def Arcs_List(n, matrix):
    matrix2 = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                a = [i, j]
                matrix2.append(a)
    return matrix2

def List_of_Successors(n, matrix):
    matrix3 = []
    for i in range(n):
        a = []
        for j in range(n):
            if matrix[i][j] == 1:
                a.append(j)
        matrix3.append(a)
    return matrix3

def Labels(n):
    a = []
    for i in range(n):
        a.append([0,0])
    return a

def dfs(visited, graph, node, order, table_of_labels):  #function for dfs
    if node not in visited:
        visited.add(node)
        order.append(node)
        table_of_labels[node][0] = len(order)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, order, table_of_labels)
        order.append(node)
        table_of_labels[node][1] = len(order)