class Node:
    def __init__(self, item):
        self.item = item
        self.left = None  # left (smaller) node
        self.right = None  # right (larger) node

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
