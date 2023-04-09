import math
from state_space_problem import StateSpaceProblem

class TspState:
    def __init__(self, visited, cur_city):
        self.visited = visited
        self.cur_city = cur_city

    def __eq__(self, other):
        return (self.visited == other.visited) and (self.cur_city == other.cur_city)
    
    def __str__(self):
        return self.visited.__str__() + " " + self.cur_city.__str__()

class Tsp(StateSpaceProblem):    
    def __init__(self, cities):
        self.cities = cities
        self.distances = [[self.compute_distance(self.cities[i], self.cities[j]) for i in range(len(cities))] for j in range(len(cities))]

    def get_init_state(self):
        return TspState([False for i in range(len(self.cities))], 0)
    
    def is_goal(self, state):
        return all(state.visited)
    
    def get_available_actions(self, state):
        actions = []
        for city_id in range(len(self.cities)):
            if not state.visited[city_id]:
                actions.append(city_id)

        return actions
    
    def get_next_state(self, state, action):
        next_state_visited = state.visited.copy()
        next_state_visited[action] = True
        next_state_cur_city = action
        return TspState(next_state_visited, next_state_cur_city)

    def get_action_cost(self, state, action):
        return self.distances[state.cur_city][action]

    def heuristic(self, state):
        # Minimum spanning tree?
        # TODO: Implement this
        return 1
    
    def compute_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)



if __name__ == "__main__":
    from tree_search import TreeSearch

    cities = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1)
    ]

    problem = Tsp(cities)
    priority_f = lambda node: node.g
    path = TreeSearch(problem, priority_f)

    for p in reversed(path):
        print(p)