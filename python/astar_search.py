from graph_search import GraphSearch

def AstarSearch(problem):
    f = lambda node: problem.heuristic(node.state) + node.g
    return GraphSearch(problem, f)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding
    from sliding_tile import SlidingTile
    problem = GridPathfinding(100, 100, goal_position=(99, 99))
    path = AstarSearch(problem)

    for s in reversed(path):
        print(s)

    tiles = SlidingTile(3, 3, init_position=[7, 4, 5, 1, 8, 3, 2, 0, 6])
    path = AstarSearch(tiles)

    for s in reversed(path):
        print(s)
