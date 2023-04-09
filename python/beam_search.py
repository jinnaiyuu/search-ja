from optimized_graph_search import OptimizedGraphSearch
from bucket_openlist import BucketOpenList
from hash_closedlist import HashClosedList

def BeamSearch(problem, priority_f, beam_width):
    init_h_value = problem.heuristic(problem.get_init_state())
    open_list = BucketOpenList(C_min=init_h_value, C_max=init_h_value*8, beam_width=beam_width)
    closed_list = HashClosedList()
    path = OptimizedGraphSearch(problem, priority_f, open_list, closed_list)
    return path

if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding(10, 10, goal_position=(9, 9))
    priority_f = lambda node: node.g

    path = BeamSearch(problem, priority_f, beam_width=5)
 
    for s in reversed(path):
        print(s)
