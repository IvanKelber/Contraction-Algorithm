import random
import copy
import math

#input_table = [[1, 5, 6, 2], [2, 1, 5, 6, 3], [3, 2, 7, 8, 4], [4, 3, 7, 8], [5, 2, 6, 1], [6, 5, 1, 2, 7], [7, 6, 3, 4, 8], [8, 7, 3, 4]]

f = open("InputGraph.txt", "r")
input_table = []
for line in f:
    string_entries = line.split()
    row = [int(n) for n in string_entries]
    input_table.append(row)

#makes a list of all current edges and deletes edges that go from a node to itself
def make_edge_list (table):
    edge_list = []
    for entry in table:
        for i in range(1, len(entry)):
            if entry[0] < entry[i]:
                edge_list.append([entry[0], entry[i]])
        i = 1
        while i < len(entry):
            while i < len(entry) and entry[0] == entry[i]:
                entry[i], entry[len(entry) - 1] = entry[len(entry) - 1], entry[i]
                entry.pop()  
            i+= 1
    return edge_list

def sort_table (table):
    new_table = [None] * len(table)
    for entry in table:
        new_table[entry[0] - 1] = entry
    return new_table


def contract_edge (table, edge_list):
    edge = random.randint(0, len(edge_list) - 1)
    p1, p2 = edge_list[edge][0], edge_list[edge][1]
    for i in range(1, len(table[p2 - 1])):
        table[p1 - 1].append(table[p2 - 1][i])
    table[p2 - 1] = [p2]
    for i in range(len(table)):
        for j in range(1, len(table[i])):
            if table[i][j] == p2:
                table[i][j] = p1
    return make_edge_list(table)




sorted = sort_table(input_table)
minimum  = len(sorted)
#for iteration in range(len(sorted)**2 * int(math.ceil(math.log(len(sorted))))):
for iteration in range(1000):
    t1 = copy.deepcopy(sorted)
    el1 = make_edge_list(t1)
        
    counter = len(t1) - 2
    for i in range(counter):
        el1 = contract_edge(t1, el1)
    print(len(el1))
    if len(el1) < minimum:
        minimum = len(el1)
print minimum
