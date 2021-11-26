global graph
global invalid_triple
global n
(n, m, k) = [int(x) for x in input().split()]
graph = {i:[] for i in range(n)}
for i in range(m):
    (first_node, second_node) = [int(x) - 1 for x in input().split()]
    graph[first_node].append(second_node)
    graph[second_node].append(first_node)

invalid_triple = {}
for i in range(k):
    (node1, node2, node3) = [int(x) - 1 for x in input().split()]
    invalid_triple[(node1, node2, node3)] = True

fringe = [{'node': 0, 'father': -1, 'cost': 0}]
closed = {}

def graph_search():
    while fringe:
        item = fringe.pop(0)
        for adjacent in graph[item['node']]:
            if not closed.get((item['node'], adjacent), False) and not invalid_triple.get((item['father'], item['node'], adjacent), False):
                if adjacent == n - 1:
                    print(item['cost'] + 1)
                    return
                new_item = {'node': adjacent, 'father': item['node'], 'cost': item['cost'] + 1}
                fringe.append(new_item)
        closed[(item['father'], item['node'])] = True
    print(-1)
graph_search()