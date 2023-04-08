from graph_search import GraphSearch

def BreadthFristSearch(problem):
    return GraphSearch(problem, lambda node: node.d)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = BreadthFristSearch(problem)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)