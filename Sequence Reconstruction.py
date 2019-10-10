from collections import deque

def sequenceReconstruction(org, seqs):
    # write your code here

    graph = {}

    for seq in seqs:
        for node in seq:
            if node not in graph:
                graph[node] = set()
    for seq in seqs:
        for i in range(len(seq)-1):
            graph[seq[i]].add(seq[i+1])


    topo_order = topological_sort(graph)
    return topo_order == org

def get_indegrees(graph):
    indegrees = {
        node: 0
        for node in graph
    }

    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1

    return indegrees
def topological_sort(graph):
    indegrees = get_indegrees(graph)

    queue = deque(node for node in graph if indegrees[node] == 0)
    # for node in graph:
    #     if indegrees[node] == 0:
    #         queue.append(node)
    print(queue)
    topo_order = []
    while queue:
        if len(queue) > 1:
            # there must exist more than one topo orders
            return None

        node = queue.pop()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == len(graph):
        return topo_order

    return None

if __name__ == '__main__':
    org  = [1,2,3]
    seqs = [[1,2],[1,3]]

    print(sequenceReconstruction(org,seqs))