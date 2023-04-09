from search_node import SearchNode
from util import SearchLogger

logger = SearchLogger()

def RecursiveSearchEngine(problem, cur_node):
    logger.expanded += 1

    if problem.is_goal(cur_node.state):
        return [cur_node]
    else:
        actions = problem.get_available_actions(cur_node.state)

        for a in actions:
            next_state = problem.get_next_state(cur_node.state, a)

            next_node = SearchNode(next_state)
            next_node.set_g(cur_node.g + problem.get_action_cost(cur_node.state, a))
            next_node.set_d(cur_node.d + 1)
            next_node.set_prev_n(cur_node)

            logger.generated += 1
            path = RecursiveSearchEngine(problem, next_node)
            if len(path) > 0:
                path.append(cur_node)
                return path
    return []

def RecursiveDepthFirstSearch(problem):
    init_state = problem.get_init_state()
    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)
    init_node.set_prev_n = 0

    logger.start()

    path = RecursiveSearchEngine(problem, init_node)

    logger.end()
    logger.print()

    return path


if __name__ == "__main__":
    from tsp import Tsp
    
    cities = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1)
    ]

    problem = Tsp(cities)
    path = RecursiveDepthFirstSearch(problem)

    for p in reversed(path):
        print(p)