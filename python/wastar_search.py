from graph_search import GraphSearch

def WAstarSearch(problem, w=1.0):
    f = lambda node: problem.heuristic(node.state) * w + node.g
    return GraphSearch(problem, f)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = WAstarSearch(problem, w=3.0)

    for s in reversed(path):
        print(s)