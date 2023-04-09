from search_node import SearchNode
from util import SearchLogger

logger = SearchLogger()

def BnBEngine(problem, cur_node, best_solution, path=None):
    logger.expanded += 1
    if problem.is_goal(cur_node.state):
        if cur_node.g < best_solution:
            best_solution = cur_node.g
            path = cur_node.get_path()
    else:
        actions = problem.get_available_actions(cur_node.state)

        for a in actions:
            next_state = problem.get_next_state(cur_node.state, a)

            next_node = SearchNode(next_state)
            next_node.set_g(cur_node.g + problem.get_action_cost(cur_node.state, a))
            next_node.set_d(cur_node.d + 1)
            next_node.set_prev_n(cur_node)

            if next_node.g + problem.heuristic(next_state) < best_solution:
                logger.generated += 1
                best_solution, path = BnBEngine(problem, next_node, best_solution, path)
            else:
                logger.pruned += 1

    return (best_solution, path)

def Branch_and_Bound(problem, best_solution=None):
    init_state = problem.get_init_state()
    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)

    if best_solution is None:
        best_solution = float('inf')

    logger.start()
    solution_cost, path = BnBEngine(problem, init_node, best_solution)

    logger.end()
    logger.print()
    return (solution_cost, path)


if __name__ == "__main__":
    from tsp import Tsp
    
    cities = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1)
    ]

    problem = Tsp(cities)
    solution_cost, path = Branch_and_Bound(problem)

    print('solution_cost=', solution_cost)
    for p in reversed(path):
        print(p)