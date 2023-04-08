def get_path(node, init_state):
    cur_node = node
    path = []
    
    while (not cur_node.state == init_state):
        path.append(cur_node)
        cur_node = cur_node.prev_n

    return path

def is_explored(node, closed_list):
    for n in closed_list:
        if (n.state == node.state) and (n.g <= node.g):
            return True
    return False

def expand(problem, state):
    next_states = []
    actions = problem.get_available_actions(state)
    for a in actions:
        next_state = problem.get_next_state(state, a)
        next_states.append(next_state)
    return next_states

def GraphSearch(problem, priority_f=None):
    class SearchNode:
        def __init__(self, state):
            self.state = state

        def set_g(self, g):
            self.g = g
        
        def set_d(self, d):
            self.d = d

        def set_prev_n(self, prev_n):
            self.prev_n = prev_n

    open = []
    closed = []

    init_state = problem.get_init_state()

    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)
    init_node.set_prev_n = 0

    open.append(init_node)
    closed.append(init_node)


    while (len(open) > 0):
        open.sort(key=lambda node: priority_f(node), reverse=True)

        node = open.pop()

        if problem.is_goal(node.state):
            return get_path(node, init_state)
        else:
            # Expand the node
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)

                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.get_action_cost(a))
                next_node.set_d(node.d + 1)
                if not is_explored(next_node, closed):
                    next_node.set_prev_n(node)
                    open.append(next_node)
                    closed.append(next_node)
    return None


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    priority_f = lambda node: node.g
    path = GraphSearch(problem, priority_f)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)