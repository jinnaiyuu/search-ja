from state_space_problem import StateSpaceProblem

class GridState:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __str__(self):
        return "(" + self.x.__str__() + ", " + self.y.__str__() + ")"

class GridPathfinding(StateSpaceProblem):
    def __init__(self, 
                 width=5, 
                 height=5, 
                 init_position=(0, 0), 
                 goal_position=(4, 4)):
        
        self.width = width
        self.height = height
        self.init_position = init_position
        self.goal_position = goal_position

        # TODO: make state class?
        self.init_state = GridState(self.init_position)

    def get_init_state(self):
        return self.init_state
    
    def is_goal(self, state):
        return (state.x == self.goal_position[0]) and (state.y == self.goal_position[1])

    def get_available_actions(self, state):
        actions = []
        if state.x > 0:
            actions.append('l')
        if state.x < self.width - 1:
            actions.append('r')
        if state.y > 0:
            actions.append('u')
        if state.y < self.height - 1:
            actions.append('d')
        return actions

    def get_next_state(self, state, action):
        if action == 'l':
            return GridState((state.x - 1, state.y))
        elif action == 'r':
            return GridState((state.x + 1, state.y))
        elif action == 'u':
            return GridState((state.x, state.y - 1))
        elif action == 'd':
            return GridState((state.x, state.y + 1))
        else:
            raise Exception("Invalid action: " + action)
        
    def get_action_cost(self, action):
        return 1

    def heuristic(self, state):
        # Manhattan distance heuristic
        return abs(state.x - self.goal_position[0]) + abs(state.y - self.goal_position[1])