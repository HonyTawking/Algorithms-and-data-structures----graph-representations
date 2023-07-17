import random
import time
import csv
import graphs_def
import sys

sys.setrecursionlimit(30000)



graphs_size = 100
graph_sizes = []
label_counting_time_1 = []
label_counting_time_2 = []
counting_return_arcs_1 = []
counting_return_arcs_2 = []
time_of_counting_return_arcs_1_1 = []
time_of_counting_return_arcs_1_2 = []
time_of_counting_return_arcs_2_1 = []
time_of_counting_return_arcs_2_2 = []
time_of_counting_return_arcs_3_1 = []
time_of_counting_return_arcs_3_2 = []


for i in range(1,11):
    n = graphs_size * i
    graph_sizes.append(n)

    matrix1 = (graphs_def.Adjacency_Matrix(n)) #density 0.2
    matrix2 = (graphs_def.Adjacency_Matrix(n)) #density 0.4

    density_1 = ((n) * (n - 1) / 2) * 0.2
    density_2 = ((n) * (n - 1) / 2) * 0.4

    ind = 0


    while(ind != density_1):
        ind1 = random.randint(0, n - 1)
        ind2 = random.randint(0, n - 1)
        if matrix1[ind1][ind2] == 0:
            matrix1[ind1][ind2] = 1
            ind +=1
    ind = 0

    while (ind != density_2):
        ind1 = random.randint(0, n - 1)
        ind2 = random.randint(0, n - 1)
        if matrix2[ind1][ind2] == 0:
            matrix2[ind1][ind2] = 1
            ind += 1

    Arcs_List_1 = graphs_def.Arcs_List(n, matrix1);
    Arcs_List_2 = graphs_def.Arcs_List(n, matrix2);

    #                       PRINT ARCS LIST
    # print("-------------------------------")
    # print(Arcs_List_1)
    # print(Arcs_List_2)
    # print("-------------------------------")

    List_of_Successors_1 = graphs_def.List_of_Successors(n, matrix1);
    List_of_Successors_2 = graphs_def.List_of_Successors(n, matrix2);

    #                       PRINT list of successors
    # print("-------------------------------")
    print(List_of_Successors_1)
    print(List_of_Successors_2)
    # print("-------------------------------")




    #                       Print matrix
    # sum1 = 0
    # for j in range(n):
    #     print(*matrix1[j])
    #     sum1 += sum(matrix1[j])
    # print("----------")

    # sum2 = 0
    # for j in range(n):
    #     print(*matrix2[j])
    #     sum2 += sum(matrix2[j])
    # print("-----",sum1, "---------------",sum2)



    # Filling the stack and table of Labels

    st = time.time()
    table_of_labels_1 = graphs_def.Labels(n)
    visited_1 = set()
    stack_1 = []


    for j in range(n):
        if j not in visited_1:
            graphs_def.dfs(visited_1,List_of_Successors_1,j,stack_1,table_of_labels_1)
    en =time.time()
    label_counting_time_1.append(en-st)


    st = time.time()
    table_of_labels_2 = graphs_def.Labels(n)
    visited_2 = set()
    stack_2 = []

    for j in range(n):
        if j not in visited_2:
            graphs_def.dfs(visited_2,List_of_Successors_2,j,stack_2,table_of_labels_2)
    en = time.time()
    label_counting_time_2.append(en - st)


    # Counting return arcs - arcs list

    loop1 = False # d[v] < d[u] < f[u] < f[v]
    st = time.time()
    cycle1 = 0
    for j in range(int(((n) * (n - 1) / 2) * 0.2)):
        u, v = Arcs_List_1[j][0], Arcs_List_1[j][1]
        if (table_of_labels_1[v][0] < table_of_labels_1[u][0] < table_of_labels_1[u][1] < table_of_labels_1[v][1]) == True:
            cycle1 +=1
        if u == v:
            cycle1 +=1
    en = time.time()
    time_of_counting_return_arcs_1_1.append(en - st)
    if cycle1>0:
        loop1 = True

    loop2 = False  # d[v] < d[u] < f[u] < f[v]
    st=time.time()
    cycle2 = 0
    for j in range(int(((n) * (n - 1) / 2) * 0.4)):
        u, v = Arcs_List_2[j][0], Arcs_List_2[j][1]
        if (table_of_labels_2[v][0] < table_of_labels_2[u][0] < table_of_labels_2[u][1] < table_of_labels_2[v][1]) == True:
            cycle2 += 1
        if u == v:
            cycle2 += 1
    en = time.time()
    time_of_counting_return_arcs_1_2.append(en-st)
    if cycle2 > 0:
        loop2 = True

    # Print number of return arcs
    print(cycle1)
    print(cycle2)
    # print("---------")
    counting_return_arcs_1.append(cycle1)
    counting_return_arcs_2.append(cycle2)

    # Counting return arcs - adjacency matrix

    loop2_1 = False  # d[v] < d[u] < f[u] < f[v]
    st = time.time()
    cycle2_1 = 0
    for j in range(n):
        for k in range(n):
            if matrix1[j][k] == 1:
                u = j
                v = k
                if j == k:
                    cycle2_1+=1
                elif (table_of_labels_1[v][0] < table_of_labels_1[u][0] < table_of_labels_1[u][1] < table_of_labels_1[v][1]) == True:
                    cycle2_1 += 1
    en = time.time()
    time_of_counting_return_arcs_2_1.append(en-st)
    if cycle2_1 > 0:
        loop2_1 = True

    loop2_2 = False  # d[v] < d[u] < f[u] < f[v]
    st = time.time()
    cycle2_2 = 0
    for j in range(n):
        for k in range(n):
            if matrix2[j][k] == 1:
                u = j
                v = k
                if j == k:
                    cycle2_2 += 1
                elif (table_of_labels_2[v][0] < table_of_labels_2[u][0] < table_of_labels_2[u][1] < table_of_labels_2[v][1]) == True:
                    cycle2_2 += 1
    en = time.time()
    time_of_counting_return_arcs_2_2.append(en - st)
    if cycle2_2 > 0:
        loop2_2 = True

    # Print number of return arcs
    print(cycle2_1)
    print(cycle2_2)
    # print("---------")

    # Counting return arcs - list of successors

    loop3_1 = False  # d[v] < d[u] < f[u] < f[v]
    st = time.time()
    cycle3_1 = 0
    for j in range(n):
        for k in range(len(List_of_Successors_1[j])):
            u = j
            v = List_of_Successors_1[j][k]
            if j == List_of_Successors_1[j][k]:
                cycle3_1 += 1
            elif (table_of_labels_1[v][0] < table_of_labels_1[u][0] < table_of_labels_1[u][1] < table_of_labels_1[v][1]) == True:
                cycle3_1 += 1
    en = time.time()
    time_of_counting_return_arcs_3_1.append(en - st)
    if cycle3_1 > 0:
        loop3_1 = True

    loop3_2 = False  # d[v] < d[u] < f[u] < f[v]
    st = time.time()
    cycle3_2 = 0
    for j in range(n):
        for k in range(len(List_of_Successors_2[j])):
            u = j
            v = List_of_Successors_2[j][k]
            if j == List_of_Successors_2[j][k]:
                cycle3_2 += 1
            elif (table_of_labels_2[v][0] < table_of_labels_2[u][0] < table_of_labels_2[u][1] < table_of_labels_2[v][1]) == True:
                cycle3_2 += 1
    en = time.time()
    time_of_counting_return_arcs_3_2.append(en - st)
    if cycle3_2 > 0:
        loop3_2 = True
        # Print number of return arcs
    print(cycle3_1)
    print(cycle3_2)
    print("---------")



# with open('grafy_czasy.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Rozmiar grafu"] + ["czas zliczania etykiet 0.2"] + ["czas zliczania etykiet 0.4"] + ["time_of_counting_return_arcs lista_ł 0.2"] + ["time_of_counting_return_arcs lista_ł 0.4"] + ["time_of_counting_return_arcs matrix 0.2"] + ["time_of_counting_return_arcs matrix 0.4"] + ["time_of_counting_return_arcs lista_n 0.2"] + ["time_of_counting_return_arcs lista_n 0.4"])
#     for i in range(len(graph_sizes)):
#         writer.writerow([graph_sizes[i]] + [label_counting_time_1[i]] + [label_counting_time_2[i]] + [time_of_counting_return_arcs_1_1[i]] + [time_of_counting_return_arcs_1_2[i]] + [time_of_counting_return_arcs_2_1[i]] + [time_of_counting_return_arcs_2_2[i]] + [time_of_counting_return_arcs_3_1[i]] + [time_of_counting_return_arcs_3_2[i]])
#
# with open('grafy_łuki.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Rozmiar grafu"] + ["łuki powrotne 0.2"] + ["łuki powrotne 0.4"])
#     for i in range(len(graph_sizes)):
#         writer.writerow([graph_sizes[i]] + [counting_return_arcs_1[i]] + [counting_return_arcs_2[i]])