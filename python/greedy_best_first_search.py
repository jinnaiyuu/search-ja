from graph_search import GraphSearch

def GreedyBestFirstSearch(problem):
    h = lambda node: problem.heuristic(node)
    return GraphSearch(problem, h)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = GreedyBestFirstSearch(problem)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)