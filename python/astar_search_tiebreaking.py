from graph_search import GraphSearch

def TiebreakingAstarSearch(problem):
    f = lambda node: (problem.heuristic(node.state) + node.g, problem.heuristic(node.state))
    return GraphSearch(problem, f)


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding
    from sliding_tile import SlidingTile

    problem = GridPathfinding()
    path = TiebreakingAstarSearch(problem)

    for s in reversed(path):
        print(s)


    tiles = SlidingTile(3, 3, init_position=[7, 4, 5, 1, 8, 3, 2, 0, 6])
    path = TiebreakingAstarSearch(tiles)

    for s in reversed(path):
        print(s)