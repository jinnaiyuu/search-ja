class StateSpaceProblem:
    def __init__(self):
        assert False

    def get_init_state(self):
        assert False

    def is_goal(self, state) -> bool:
        assert False

    def get_available_actions(self, state):
        assert False

    def get_next_state(self, state, action):
        assert False

    def get_action_cost(self, state, action):
        assert False

    def heuristic(self, state):
        assert False
