grath = {}
grath['start'] = {}
grath['start']['a'] = 6
grath['start']['b'] = 2
grath['a'] = {}
grath['a']['end'] = 1
grath['b'] = {}
grath['b']['end'] = 5
grath['b']['a'] = 3
grath['end'] = {}
# print(grath)

infinite = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinite
# print(cost)

fathers = {}
fathers['a'] = 'start'
fathers['b'] = 'start'
fathers['end'] = None
# print(fathers)

processed = []


def find_lower_cost(costs):
    lower_cost = float('inf')
    node_lower_cost = None
    for node in costs:
        node_cost = costs[node]
        if node_cost < lower_cost and node not in processed:
            lower_cost = node_cost
            node_lower_cost = node
    return node_lower_cost



node = find_lower_cost(costs)
while node is not None:
    cost = costs[node]
    neighbor = grath[node]
    for n in neighbor.keys():
        new_cost = cost + neighbor[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            fathers[n] = node
    processed.append(node)
    node = find_lower_cost(costs)


print("Shortest path:")
current_node = 'end'
shortest_path = ['end']
while current_node != 'start':
    current_node = fathers[current_node]
    shortest_path.append(current_node)
shortest_path.reverse()
print(shortest_path)
