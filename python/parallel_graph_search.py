from threading import Thread, Lock
from multiprocessing import Value, Array
import queue

from search_node import SearchNode
from util import SearchLogger

from bucket_openlist import BucketOpenList
from hash_closedlist import HashClosedList

def terminate_detection(has_job, terminating, confirm_terminating, n_threads, thread_id):
    if not has_job:
        terminating[thread_id] = True

        for i in range(n_threads):
            if not terminating[i]:
                return False
        confirm_terminating[thread_id] = True

        for i in range(n_threads):
            if not confirm_terminating[i]:
                return False
        return True
    else:
        terminating[thread_id] = False
        confirm_terminating[thread_id] = False
        return False

def search_thread(problem,
                  priority_f,
                  open, 
                  closed, 
                  buffers, 
                  n_threads, 
                  thread_id, 
                  incumbent_cost, 
                  incumbent_goal_node_pos, 
                  incumbent_lock,
                  terminating,
                  confirm_terminating,
                  logging):

    terminating[thread_id] = False
    confirm_terminating[thread_id] = False

    while (True):
        while not buffers[thread_id].empty():
            recv_node = buffers[thread_id].get()
            f = priority_f(recv_node)
            if (not closed.is_explored(recv_node)) and (f < incumbent_cost.value):
                open.push(recv_node, f)
                closed.push(recv_node)
                logging.generated += 1
            else:
                logging.pruned += 1

        if terminate_detection(len(open) > 0, terminating, confirm_terminating, n_threads, thread_id):
            break

        if (len(open) == 0):
            continue

        node = open.pop()
        logging.expanded += 1

        if problem.is_goal(node.state) and (node.g < incumbent_cost.value):
            incumbent_lock.acquire()
            incumbent_cost.value = node.g
            idx = closed.find(node)
            incumbent_goal_node_pos[0] = thread_id
            incumbent_goal_node_pos[1] = idx[0]
            incumbent_goal_node_pos[2] = idx[1]
            print("incumbent solution updated: ", incumbent_cost.value)
            incumbent_lock.release()
        else:
            # Expand the node
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)

                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.get_action_cost(node.state, a))
                next_node.set_d(node.d + 1)
                next_node.set_prev_n(node)

                f = priority_f(next_node)
                if  (f < incumbent_cost.value):
                    dst = hash(next_state) % n_threads
                    buffers[dst].put(next_node)

    return

def HashDistributedGraphSearch(problem, priority_f=None, n_threads=2):

    init_state = problem.get_init_state()

    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)
    init_node.set_prev_n = 0

    init_dst = hash(init_state) % n_threads

    init_h_value = priority_f(init_node)
    opens = [BucketOpenList(C_min=init_h_value, C_max=init_h_value*8)] * n_threads
    closeds = [HashClosedList()] * n_threads

    opens[init_dst].push(init_node, priority_f(init_node))
    closeds[init_dst].push(init_node)

    # Data structure to keep the incumbent solution
    incumbent_lock = Lock()
    incumbent_cost = Value('f', 1000000000000000.0)
    incumbent_goal_node_pos = Array('i', [0, 0, 0])

    # Data structure to keep the termination status
    terminating = Array('b', [False] * n_threads)
    confirm_terminating = Array('b', [False] * n_threads)

    # Buffer for asynchronous message passing
    waiting_buffers = [queue.Queue() for i in range(n_threads)]

    loggings = [SearchLogger() for i in range(n_threads)]
    threads = []
    for i in range(n_threads):

        t = Thread(target=search_thread, 
                   args=(problem,
                         priority_f,
                         opens[i], 
                         closeds[i], 
                         waiting_buffers, 
                         n_threads, 
                         i, 
                         incumbent_cost, 
                         incumbent_goal_node_pos, 
                         incumbent_lock,
                         terminating,
                         confirm_terminating,
                         loggings[i]))
        threads.append(t)

    global_logger = SearchLogger()

    global_logger.start()

    for i in range(n_threads):
        threads[i].start()

    for i in range(n_threads):
        threads[i].join()


    pos = incumbent_goal_node_pos.get_obj()
    incumbent_goal_node = closeds[pos[0]].get_by_index(pos[1], pos[2])
    path = incumbent_goal_node.get_path()

    global_logger.end()
    global_logger.expanded = sum([l.expanded for l in loggings])
    global_logger.generated = sum([l.generated for l in loggings])
    global_logger.pruned = sum([l.pruned for l in loggings])
    global_logger.print()

    return path

if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding
    from sliding_tile import SlidingTile

    grid = GridPathfinding()
    priority_f = lambda node: node.g + grid.heuristic(node.state)
    path = HashDistributedGraphSearch(grid, priority_f, n_threads=4)

    for s in reversed(path):
        print(s)


    tiles = SlidingTile(3, 3, init_position=[7, 4, 5, 1, 8, 3, 2, 0, 6])
    priority_f_tiles = lambda node: node.g + tiles.heuristic(node.state)
    path = HashDistributedGraphSearch(tiles, priority_f_tiles, n_threads=4)

    for s in reversed(path):
        print(s)
