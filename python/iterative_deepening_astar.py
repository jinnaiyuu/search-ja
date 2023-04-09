from depth_first_iterative_deepening import IterativeDeepening

def IterativeDeepeningAstar(problem):
    return IterativeDeepening(problem, lambda node: node.g + problem.heuristic(node.state))

if __name__ == "__main__":
    from tsp import Tsp
    
    cities = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1)
    ]

    problem = Tsp(cities)
    path = IterativeDeepeningAstar(problem)

    for p in reversed(path):
        print(p)