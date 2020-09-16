
def min_cost_to_connect_nodes(nodes, edges, new_edges):
    """
    Parameters
    ----------
    nodes: int
        Total number of nodes
    edges: list
        Integer pairs representing the nodes already connected by an edge
    new_edges: list
        Integer triplets representing the pair of nodes between which an edge can be added and the
        cost of addition.

    """

    union_find = {}

    # create union find for the initial edges given
    def find(edge):
        union_find.setdefault(edge, edge)
        if union_find[edge] != edge:
            union_find[edge] = find(union_find[edge])
        return union_find[edge]

    def union(edge1, edge2):
        union_find[find(edge1)] = find(edge2)

    for e1, e2 in edges:
        if find(e1) != find(e2):
            union(e1, e2)

    # sort the new edges by cost
    # if an edge is not part of the minimum spanning tree, then include it, else continue
    cost_ret = 0
    for c1, c2, cost in sorted(new_edges, key=lambda x: x[2]):
        if find(c1) != find(c2):
            union(c1, c2)
            cost_ret += cost

    if len({find(c) for c in union_find}) == 1 and len(union_find) == nodes:
        return cost_ret
    else:
        return -1
