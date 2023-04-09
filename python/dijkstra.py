from graph_search import GraphSearch

def DijkstraSearch(problem):
    return GraphSearch(problem, lambda node: node.g)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = DijkstraSearch(problem)

    for s in reversed(path):
        print(s)