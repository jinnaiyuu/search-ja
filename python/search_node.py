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

    def get_path(self):
        cur_node = self
        path = []
        
        while (cur_node is not None and hasattr(cur_node, 'prev_n')):
            path.append(cur_node)
            cur_node = cur_node.prev_n

        return path