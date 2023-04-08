def get_path(node, init_state):
    cur_node = node
    path = []
    
    while (not cur_node.state == init_state):
        path.append(cur_node)
        cur_node = cur_node.prev_n

    return path

def OptimizedGraphSearch(problem, priority_f, open_list, closed_list):
    class SearchNode:
        def __init__(self, state):
            self.state = state

        def set_g(self, g):
            self.g = g
        
        def set_d(self, d):
            self.d = d

        def set_prev_n(self, prev_n):
            self.prev_n = prev_n

    init_state = problem.get_init_state()

    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)
    init_node.set_prev_n = 0

    open_list.push(init_node, priority_f(init_node))
    closed_list.push(init_node)

    while (len(open_list) > 0):
        node = open_list.pop()

        if problem.is_goal(node.state):
            return get_path(node, init_state)
        else:
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)

                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.get_action_cost(a))
                next_node.set_d(node.d + 1)

                if not closed_list.explored(next_node):
                    next_node.set_prev_n(node)
                    open_list.push(next_node, priority_f(next_node))
                    closed_list.push(next_node)
    return None


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding
    from bucket_openlist import BucketOpenList
    from hash_closedlist import HashClosedList

    problem = GridPathfinding()
    priority_f = lambda node: node.g

    init_h_value = problem.heuristic(problem.get_init_state())
    open_list = BucketOpenList(C_min=init_h_value, C_max=init_h_value*8)
    closed_list = HashClosedList()
    path = OptimizedGraphSearch(problem, priority_f, open_list, closed_list)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)