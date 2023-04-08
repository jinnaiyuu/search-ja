def get_path(node):
    cur_node = node
    path = []
    
    while (cur_node is not None and hasattr(cur_node, 'prev_n')):
        path.append(cur_node)
        cur_node = cur_node.prev_n

    return path

def TreeSearch(problem, priority_f=None):
    class SearchNode:
        def __init__(self, state):
            self.state = state

        def set_g(self, g):
            self.g = g
        
        def set_d(self, d):
            self.d = d

        def set_prev_n(self, prev_n):
            self.prev_n = prev_n

        def __str__(self):
            return self.state.__str__() + ": g=" + str(self.g) + ", d=" + str(self.d)

    open = []

    ### closed list is not used in tree search.
    ### We use it on graph_search for duplicate detection.
    # closed = []

    init_state = problem.get_init_state()

    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)
    init_node.set_prev_n = 0

    open.append(init_node)

    while (len(open) > 0):
        open.sort(key=lambda node: priority_f(node), reverse=True)

        node = open.pop()

        if problem.is_goal(node.state):
            return get_path(node)
        else:
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)

                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.get_action_cost(a))
                next_node.set_d(node.d + 1)
                next_node.set_prev_n(node)
                open.append(next_node)

    return None


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    priority_f = lambda node: node.g
    path = TreeSearch(problem, priority_f)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)