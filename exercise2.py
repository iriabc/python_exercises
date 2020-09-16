from collections import deque


def minimum_route_to_treasure(the_map):
    """
    Calculates the minimum route to the treasure for a given map.
    The route starts from 0, 0 and can move one block up, down, left or right at a time.

    Parameters
    ----------
    the_map: list of lists
        Matrix containing the points of the map
        e.g.
        [
            [‘O’, ‘O’, ‘O’, ‘O’],
            [‘D’, ‘O’, ‘D’, ‘O’],
            [‘O’, ‘O’, ‘O’, ‘O’],
            [‘X’, ‘D’, ‘D’, ‘O’],
        ]
    Map with different features:
    - O is a point you can sail in
    - D is a dangerous point you can't sail in
    - X is the point with the treasure

    """

    # Map dimensions
    width = len(the_map)
    height = len(the_map[0])

    # Check that the map has some dimensions
    if width == 0 or height == 0:
        raise ValueError("Please provide a valid map")

    # Define start point and features
    start = (0, 0)
    treasure = "X"
    danger = "D"

    # Create a queue to store the track
    queue = deque([[start]])
    visited = [start]

    # Find the path
    while queue:
        path = queue.popleft()
        x, y = path[-1]

        # Check if we have found the treasure
        if the_map[x][y] == treasure:
            return path

        # Move using one of the possible movements
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and the_map[x2][y2] != danger \
                    and (x2, y2) not in visited:
                queue.append(path + [(x2, y2)])
                visited.append((x2, y2))
