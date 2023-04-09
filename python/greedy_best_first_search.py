from graph_search import GraphSearch

def GreedyBestFirstSearch(problem):
    h = lambda node: problem.heuristic(node.state)
    return GraphSearch(problem, h)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = GreedyBestFirstSearch(problem)

    for s in reversed(path):
        print(s)