class Graph(object):
    def __init__(self, n_vertices=0):
        self.n_vertices = n_vertices
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = {v: weight}
        else:
            self.adj_list[u][v] = weight


def dfs(g, vertex):
    dfs_visit(g, vertex)

def dfs_visit(g, v, parent=None, relation_str=''):
    if parent:
        relation_str += g.adj_list[parent][v]
        if relation_str == relation_test:
            print 1
            import sys
            sys.exit()

    if len(relation_str) > len(relation_test):
        return

    for item in g.adj_list[v]:
        dfs_visit(g, item, v, relation_str)


def create_graph(g, matrix):
    for i, line in enumerate(matrix):
        for j, relation in enumerate(line):
            if i != j:
                g.add_edge(i, j, relation)


n = int(raw_input())
matrix = []
for line in xrange(n):
    str = raw_input()
    matrix.append(str)
first = int(raw_input())
second = int(raw_input())

relation_test = raw_input()

g = Graph()
create_graph(g, matrix)

#print g.adj_list

result = False
answer = False

dfs(g, first)
dfs(g, second)

print 0

