from graph_search import GraphSearch

def DijkstraSearch(problem):
    return GraphSearch(problem, lambda node: node.g)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = DijkstraSearch(problem)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)