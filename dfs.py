import sys

from maze import Maze, path_from, Node


def dfs(mazeI, nodeI: Node):
    if nodeI is None:
        nodeI = mazeI.find_node('S')
    nodeI.visited = True
    if nodeI.type == 'E':
        return path_from(nodeI)

    # if the node is not the exit we look for neighbor
    children = mazeI.get_possible_movements(nodeI)

    for child in children:
        if not child.visited:
            child.parent = nodeI
            odp = dfs(mazeI, child)
            if odp is not None:
                return odp
    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = dfs(maze, None)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()
