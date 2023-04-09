from state_space_problem import StateSpaceProblem

class TileState:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return (self.tile == other.tile)

    def __hash__(self):
        return hash(tuple(self.tile))
    
    def __str__(self):
        return self.tile.__str__()

class SlidingTile(StateSpaceProblem):
    def __init__(self, 
                 width=3, 
                 height=3, 
                 init_position=[1, 0, 2, 3, 4, 5, 6, 7, 8]):
        
        self.width = width
        self.height = height
        self.init_position = init_position
        self.goal_position = [i for i in range(0, width*height)]

        assert(len(self.init_position) == self.width * self.height)

        # TODO: make state class?
        self.init_state = TileState(self.init_position)

    def get_init_state(self):
        return self.init_state
    
    def is_goal(self, state):
        return state.tile == self.goal_position 
    
    def get_available_actions(self, state):
        blank_position = state.tile.index(0)

        b_pos_x = blank_position % self.width
        b_pos_y = blank_position // self.width

        actions = []
        if b_pos_x > 0:
            actions.append('l')
        if b_pos_x < self.width - 1:
            actions.append('r')
        if b_pos_y > 0:
            actions.append('d')
        if b_pos_y < self.height - 1:
            actions.append('u')

        return actions
    
    def get_next_state(self, state, action):
        blank_position = state.tile.index(0)

        next_state_tile = state.tile.copy()
        if action == 'l':
            next_blank_position = blank_position - 1
        elif action == 'r':
            next_blank_position = blank_position + 1
        elif action == 'd':
            next_blank_position = blank_position - self.width
        elif action == 'u':
            next_blank_position = blank_position + self.width
       
        sliding_tile = state.tile[next_blank_position]
        next_state_tile[blank_position] = sliding_tile
        next_state_tile[next_blank_position] = 0

        return TileState(next_state_tile)

    def get_action_cost(self, state, action):
        return 1

    def heuristic(self, state):
        # Manhattan distance heuristic
        return self.manhattan_distance(state)
    
    def manhattan_distance(self, state):
        dist = 0
        for tile_id in range(1, len(state.tile)):
            position = state.tile.index(tile_id)

            pos_x = position % self.width
            pos_y = position // self.width

            goal_x = tile_id % self.width
            goal_y = tile_id // self.width

            dist += abs(goal_x - pos_x) + abs(goal_y - pos_y)
        return dist
    



if __name__ == "__main__":
    from tree_search import TreeSearch

    problem = SlidingTile(3, 3, init_position=[1, 2, 0, 3, 4, 5, 6, 7, 8])
    priority_f = lambda node: node.g
    path = TreeSearch(problem, priority_f)

    print(problem.get_init_state())
    for p in reversed(path):
        print(p)

        