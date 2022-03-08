import sys

from maze import Maze, path_from


def bfs(maze):
    start_node = maze.find_node('S')
    q = [start_node]
    while len(q) > 0:
        node = q.pop(0)  # FIFO
        node.visited = True
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            if not child.visited:
                child.parent = node
                q.append(child)

    return None


def dfs_search(maze):
    # find the start
    start_node = maze.find_node('S')
    print(start_node.parent)



def dfs(maze):
    start_node = maze.find_node('S')


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = bfs(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()
dfs_search(maze)