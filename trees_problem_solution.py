class Maze():

    class Node():
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None
    
    def __init__(self):
        self.root = None
    

    def insert(self, data):
        if self.root is None:
            self.root = Maze.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left == None:
                node.left = Maze.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right == None:
                node.right = Maze.Node(data)
            else:
                self._insert(data, node.right)
    

    def insert_node(self, insert_node):
        if self.root is None:
            self.root = insert_node
        else:
            self._insert_node(insert_node, self.root)

    def _insert_node(self, insert_node, node):
        if insert_node.data < node.data:
            if node.left == None:
                node.left = insert_node
            else:
                self._insert_node(insert_node, node.left)
        elif insert_node.data > node.data:
            if node.right == None:
                node.right = insert_node
            else:
                self._insert_node(insert_node, node.right)
        

    def __contains__(self, data):
        return self._contains(data, self.root)

    def _contains(self, data, node):
        if node != None:
            if data == node.data:
                return True
            if data < node.data:
                return self._contains(data, node.left)
            if data > node.data:
                return self._contains(data, node.right)


    def remove_branch(self, data, node):
        if node.right != None:
            if data == node.right.data:
                temp_node = node.right
                node.right = None
                return temp_node
            elif data > node.data:
                return self.remove_branch(data, node.right)
        if node.left != None:
            if data == node.left.data:
                temp_node = node.left
                node.left = None
                return temp_node
            elif data < node.data:
                return self.remove_branch(data, node.left)



def create_maze_from_sorted_list(sorted_list):
    maze = Maze() 
    insert_middle(sorted_list, 0, len(sorted_list)-1, maze)
    return maze


def insert_middle(sorted_list, first, last, maze):
    if (0 <= first <= len(sorted_list)) and (0 <= last <= len(sorted_list)): 
        middle_index = (first + last) // 2
        maze.insert(sorted_list[middle_index])
        if middle_index != first:
            insert_middle(sorted_list, middle_index, last, maze)
        if middle_index != last:
            insert_middle(sorted_list, first, middle_index, maze)


sorted_list = []
for i in range(100 + 1):
    sorted_list.append(i + 1)
maze = create_maze_from_sorted_list(sorted_list)

print(42 in maze)
print(1 in maze)
print(100 in maze)
print(1000 in maze)

print()

print(42 in maze)
blocked_off_portion = maze.remove_branch(42, maze.root)
print(42 in maze)
maze.insert_node(blocked_off_portion)
print(42 in maze)