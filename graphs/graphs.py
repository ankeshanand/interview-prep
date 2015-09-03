class Graph(object):
    def __init__(self, weighted=False, undirected=False):
        self.adj_list = {}
        self.vertices = set()
        self.weighted = weighted
        self.undirected = undirected

    def add_edge(self, u, v, weight=None):
        if not self.weighted:
            self.adj_list[u] = self.adj_list.get(u, [])
            self.adj_list[u].append(v)

            if self.undirected:
                self.adj_list[v] = self.adj_list.get(v, [])
                self.adj_list[v].append(u)

        else:
            # for weighted graphs
            self.adj_list[u] = self.adj_list.get(u, {})
            self.adj_list[u][v] = weight

            if self.undirected:
                self.adj_list[v] = self.adj_list.get(v, {})
                self.adj_list[v][u] = weight

        self.vertices.add(u)
        self.vertices.add(v)

    def neighbours(self, vertex):
        return self.adj_list.get(vertex, iter([]))


class DFSResult(object):
    """ Container to hold the results of a DFS Traversal. """

    def __init__(self):
        self.parent = {}
        self.finished = {}
        self.order = []


def dfs(g):
    results = DFSResult()
    for vertex in g.vertices:
        if vertex not in results.parent:
            dfs_visit(g, vertex, results)
    return results


def dfs_visit(g, vertex, results, parent=None):
    results.parent[vertex] = parent

    for neighbour in g.neighbours(vertex):
        if neighbour not in results.parent:
            dfs_visit(g, neighbour, results, vertex)

        elif neighbour not in results.finished:
            # Back edge encountered, there is a cycle
            pass

        # there are some other cases for forward edge and
        # cross edge in directed graphs

    results.finished[vertex] = True
    results.order.append(vertex)


def topological_sort(g):
    dfs_result = dfs(g)
    dfs_result.order.reverse()
    return dfs_result.order


from collections import deque

class BFSResult():
    def __init__(self):
        self.parent = {}
        self.level = {}


def bfs(g, s):
    '''Queue-based implementation of BFS.'''
    results = BFSResult()
    results.parent[s] = None
    results.level[s] = 0

    queue = deque()
    queue.append(s)

    while queue:
        v = queue.popleft()
        for neighbour in g.neighbours(v):
            if neighbour not in results.level:
                results.parent[neighbour] = v
                results.level[neighbour] = results.level[v] + 1
                queue.append(neighbour)

    return results


class DjikstraResult():
    def __init__(self):
        self.dist = {}
        self.parent = {}


def djikstra(g, s):
    """ Djikstra implementation without Priority Queues.
    Complexity: O(|V|*deletemin + (|V+E|)*insert) = O(|V|^2)

    Couldn't use priority queue because Python doesn't provide a
    decrease key method and it's tough to implement.
    """

    results = DjikstraResult()
    results.dist = {x: float('inf') for x in g.vertices}
    results.dist[s] = 0
    results.parent[s] = None

    unvisited = g.vertices

    while unvisited:
        # get vertex with minimum distance (Extract Min)
        nv = None
        for v in results.dist:
            if v in unvisited:
                if results.dist[v] < results.dist.get(nv, float('inf')):
                    nv = v

        if nv is None:
            break

        unvisited.remove(nv)

        for n in g.neighbours(nv):
            if results.dist[n] > results.dist[nv] + g.adj_list[nv][n]:
                # Relax(nv, n, weight)
                results.dist[n] = results.dist[nv] + g.adj_list[nv][n]
                results.parent[n] = nv

    return results


if __name__ == '__main__':
    g = Graph(undirected=True)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,0)

    dfs_result = dfs(g)
    print dfs_result.parent

    topological_order = topological_sort(g)
    print topological_order

    bfs_result = bfs(g, 0)
    print bfs_result.level

    g = Graph(weighted=True)
    g.add_edge(0,1,4)
    g.add_edge(0,2,2)
    g.add_edge(1,2,3)
    g.add_edge(1,4,2)
    g.add_edge(2,0,5)

    djikstra_result = djikstra(g, 1)
    print djikstra_result.dist
