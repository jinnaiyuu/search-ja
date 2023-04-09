from search_node import SearchNode
from util import SearchLogger

logger = SearchLogger()

def CLDFS_DFID(problem, cur_node, max_priorty, priority_f):
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

            if priority_f(next_node) <= max_priorty:
                logger.generated += 1
                path = CLDFS_DFID(problem, next_node, max_priorty, priority_f)
                if len(path) > 0:
                    path.append(cur_node)
                    return path
            else:
                logger.pruned += 1
    return []

def IterativeDeepening(problem, priority_f):
    logger.start()
    max_priorty = 1
    path = []

    while len(path) == 0:
        init_state = problem.get_init_state()
        init_node = SearchNode(init_state)
        init_node.set_g(0)
        init_node.set_d(0)
        init_node.set_prev_n = 0
        
        path = CLDFS_DFID(problem, init_node, max_priorty, priority_f)

        max_priorty += 1

    logger.end()
    logger.print()
    return path


def DepthFirstIterativeDeepening(problem):
    return IterativeDeepening(problem, lambda node: node.g)

if __name__ == "__main__":
    from tsp import Tsp
    
    cities = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1)
    ]

    problem = Tsp(cities)
    path = DepthFirstIterativeDeepening(problem)

    for p in reversed(path):
        print(p)