from graph_search import GraphSearch

def WAstarSearch(problem, w=1.0):
    f = lambda node: problem.heuristic(node) * w + node.g
    return GraphSearch(problem, f)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = WAstarSearch(problem, w=3.0)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)