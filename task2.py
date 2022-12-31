from collections import deque

SYMBOL = '.'
CHECKED_SYMBOL = 'x'


def path_finder(maze: str) -> int or bool:
    table = list(map(list, maze.split("\n")))
    max_len = len(table[0]) - 1
    if max_len == 0:
        return 0

    stack = deque()
    stack.append([0, 0])
    history = {(0, 0): None}
    result = False

    while stack:
        element = stack.pop()

        x = element[1]
        y = element[0]

        if element == [max_len, max_len]:
            result = True
            break

        if table[y][x] == CHECKED_SYMBOL:
            continue

        # Check right
        if max_len >= y and max_len >= x + 1 and table[y][x + 1] == SYMBOL and table[y][x + 1] != CHECKED_SYMBOL:
            stack.appendleft([y, x + 1])
            history[y, x + 1] = [y, x]

        # Check down
        if max_len >= y + 1 and max_len >= x and table[y + 1][x] == SYMBOL and table[y + 1][x] != CHECKED_SYMBOL:
            stack.appendleft([y + 1, x])
            history[y + 1, x] = [y, x]

        # Check up
        if y - 1 >= 0 and x >= 0 and table[y - 1][x] == SYMBOL and table[y - 1][x] != CHECKED_SYMBOL:
            stack.appendleft([y - 1, x])
            history[y - 1, x] = [y, x]

        # Check left
        if y >= 0 and x - 1 >= 0 and table[y][x - 1] == SYMBOL and table[y][x - 1] != CHECKED_SYMBOL:
            stack.appendleft([y, x - 1])
            history[y, x - 1] = [y, x]

        table[y][x] = CHECKED_SYMBOL

    if not result:
        return False

    current = history[max_len, max_len]
    path = [current]

    while current != [0, 0]:
        if current is None:
            break

        x = current[1]
        y = current[0]

        current = history[y, x]
        path.append(current)

    return len(path)
####################################################################################

"""
Task

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
"""


def path_finder(maze):
    maze_arr = maze_str_to_array(maze)
    n = len(maze_arr)
    start, goal = (0, 0), (n - 1, n - 1)
    return ai_star(maze_arr, start, goal)


def bfs(maze_arr, start, goal):
    """
    Implementation of breadth first search algorithm for solving maze problem
    :param maze_arr: search space
    :param start: starting node
    :param goal: goal node
    :return: True if goal can be reached
    """
    from queue import Queue
    to_be_expanded = Queue()
    to_be_expanded.put(start)
    tree = set()

    while not to_be_expanded.empty():
        node = to_be_expanded.get()
        if node == goal:
            return True
        tree.add(node)
        neighbors = get_node_neighbors(maze_arr, node)
        for neighbor in neighbors:
            if neighbor not in tree:
                to_be_expanded.put(neighbor)
    return False


def ai_star(maze_arr, start, goal):
    """
    Implementation of A* algorithm for solving maze problem. Heap is used. The value passed to
    a heap is a tuple containing priority (estimated cost) and cell coordinates.
    :param maze_arr: search space
    :param start: starting node
    :param goal: goal node
    :return: True if goal can be reached
    """
    from heapq import heappush, heappop
    to_be_expanded = []
    heappush(to_be_expanded, (manhattan_distance(start, goal), 0, 0, start))
    tree = set()

    while to_be_expanded:
        _, cost, real_cost, node = heappop(to_be_expanded)
        if node == goal:
            return real_cost
        tree.add(node)
        neighbors = get_node_neighbors(maze_arr, node)
        for neighbor in neighbors:
            if neighbor not in tree:
                heappush(to_be_expanded, (cost + manhattan_distance(neighbor, goal), cost + 0.99, real_cost + 1, neighbor))
    return False


def manhattan_distance(cell, goal):
    """
    Computes manhattan distance from some cell to the goal.
    :param cell: cell from where the distance is measured
    :param goal: goal node
    :return: absolute integer value of a manhattan distance
    """
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


def euclidean_distance(cell, goal):
    """
    Computes euclidean distance from some cell to the goal.
    :param cell: cell from where the distance is measured
    :param goal: goal node
    :return: absolute float value of a euclidean distance
    """
    from math import sqrt
    return sqrt((cell[0] - goal[0])**2 + (cell[1] - goal[1])**2)


def maze_str_to_array(maze):
    """
    Function to convert string representation of a maze into multidimensional list. One (1) represents empty
    field, zero (0) represents a wall (impenetrable field)
    :param maze: string representation of a maze
    :return: list representation of a maze.
    """
    return [[1 if char == '.' else 0 for char in row] for row in maze.split('\n')]


def get_node_neighbors(maze_arr, parent_node):
    """
    Computes a list of SearchNodes with all valid neighbors (except walls and cells out of board)
    :param maze_arr: a multidim list containing the maze
    :param parent_node: a node for with neighbors are calculated
    :return a list containing all possible neighbors
    """
    n = len(maze_arr)
    neighbors = []
    x_0, y_0 = parent_node
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x_1 = x_0 + dx
        y_1 = y_0 + dy
        if 0 <= x_1 < n and 0 <= y_1 < n and maze_arr[y_1][x_1] == 1:
            neighbors.append((x_1, y_1))
    return neighbors

