class Node:
    def __init__(self, data, level, score):
        self.data = data
        self.level = level
        self.score = score
        self.children = []
        self.parents = [self]

    def find(self, char):
        for x in range(0, len(self.data)):
            for y in range(0, len(self.data)):
                if self.data[x][y] == char:
                    return x, y

    def expand_children(self):
        x, y = self.find(0)
        #[up, down, left, right]
        moves = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        for move_x, move_y in moves:
            child = self.move_with_blank(x, y, move_x, move_y)
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                child_node.parents += self.parents
                self.children.append(child_node)
        return self.children

    def move_with_blank(self, blank_x, blank_y, move_x, move_y):
        if move_x >= 0 and move_x < len(
                self.data) and move_y >= 0 and move_y < len(
                self.data):
            copy_data = []
            copy_data = self.copy(self.data)
            copy_data[blank_x][blank_y], copy_data[move_x][move_y] = copy_data[move_x][move_y], copy_data[blank_x][blank_y]
            return copy_data
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
