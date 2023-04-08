from graph_search import GraphSearch

def TiebreakingAstarSearch(problem):
    f = lambda node: (problem.heuristic(node.state) + node.g, problem.heuristic(node.state))
    return GraphSearch(problem, f)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = TiebreakingAstarSearch(problem)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)