from search_node import SearchNode
from util import SearchLogger

def OptimizedGraphSearch(problem, priority_f, open_list, closed_list):

    init_state = problem.get_init_state()

    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)

    logger = SearchLogger()
    logger.start()

    open_list.push(init_node, priority_f(init_node))
    closed_list.push(init_node)

    while (len(open_list) > 0):
        node = open_list.pop()
        logger.expanded += 1

        if problem.is_goal(node.state):
            logger.end()
            logger.print()
            return node.get_path()
        else:
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)

                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.get_action_cost(node.state, a))
                next_node.set_d(node.d + 1)

                if not closed_list.is_explored(next_node):
                    next_node.set_prev_n(node)
                    open_list.push(next_node, priority_f(next_node))
                    closed_list.push(next_node)
                    logger.generated += 1
                else:
                    logger.pruned += 1

    logger.end()
    logger.print()
    return None


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding
    from sliding_tile import SlidingTile
    from bucket_openlist import BucketOpenList
    from hash_closedlist import HashClosedList

    # problem = GridPathfinding(100, 100, goal_position=(99, 99))
    # priority_f = lambda node: node.g + problem.heuristic(node.state)

    # init_h_value = problem.heuristic(problem.get_init_state())
    # open_list = BucketOpenList(C_min=init_h_value, C_max=init_h_value*8)
    # closed_list = HashClosedList()
    # path = OptimizedGraphSearch(problem, priority_f, open_list, closed_list)

    # for s in reversed(path):
    #     print(s)

    tiles = SlidingTile(3, 3, init_position=[7, 4, 5, 1, 8, 3, 2, 0, 6])
    priority_f = lambda node: node.g + tiles.heuristic(node.state)

    init_h_value = tiles.heuristic(tiles.get_init_state())
    open_list = BucketOpenList(C_min=init_h_value, C_max=init_h_value*8)
    closed_list = HashClosedList()
    path = OptimizedGraphSearch(tiles, priority_f, open_list, closed_list)

    for s in reversed(path):
        print(s)