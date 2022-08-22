class Node:
    def __init__(self, item):
        self.item = item
        self.left = None  # left (smaller) node
        self.right = None  # right (larger) node

    def is_leaf_node(self) -> bool:
        return self.count_children() == 0

    def count_children(self) -> int:
        count = 0
        if self.get_left() is not None:
            count += 1
        if self.get_right() is not None:
            count += 1
        return count

    def set_left(self, node):
        self.left = node
        return node

    def set_right(self, node):
        self.right = node
        return node

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_item(self):
        return self.item
