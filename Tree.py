from enum import Enum, auto

import Node


class TraverseOrder(Enum):
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()


# Binary search tree (BST)
class Tree:
    def __init__(self, root_node, name=''):
        self.root = root_node
        self.name = name
        self.height = 0
        self.tree_list = []  # flat list representation of tree traversal

    def __str__(self):
        return str(self.root.get_item())

    def get_tree_list(self):
        return self.tree_list

    def get_name(self):
        return self.name

    def get_root_node(self):
        return self.root

    def get_height(self) -> int:
        self.height = 0
        return self.get_node_height(self.root, 0)

    def get_node_height(self, node, height) -> int:
        left_height = height
        right_height = height
        if node.get_left():
            left_height = self.get_node_height(node.get_left(), left_height + 1)
        if node.get_right():
            right_height = self.get_node_height(node.get_right(), right_height + 1)
        return max(left_height, right_height)

    def search_node(self, item):
        """
        Search item in BST starting at root node
        """
        next_node = self.root
        while next_node:
            if item < next_node.get_item():
                next_node = next_node.get_left()
            elif item > next_node.get_item():
                next_node = next_node.get_right()
            else:  # found it
                return next_node
        return None

    def add_node(self, new_node: Node):
        next_node = self.root
        while next_node:
            # insert left of parent
            if new_node.get_item() < next_node.get_item():
                if next_node.get_left():
                    next_node = next_node.get_left()
                else:
                    # add new node to the left of next_node
                    next_node.set_left(new_node)
                    # print(f'Added {new_node.get_item()} left of {next_node.get_item()}')
                    return new_node
            # insert right of parent
            elif new_node.get_item() > next_node.get_item():
                if next_node.get_right():
                    next_node = next_node.get_right()
                else:
                    # add new node to the right of next_node
                    next_node.set_right(new_node)
                    # print(f'Added {new_node.get_item()} right of {next_node.get_item()}')
                    return new_node
            else:
                # cannot insert node with existing value
                return None

    def traverse(self, order: TraverseOrder):
        print(f'\nTraverse tree: {self.get_name()}')
        self.tree_list.clear()
        self.traverse_node(self.get_root_node(), order)
        print(f'Traversal order: {self.tree_list}')

    def traverse_node(self, start_node, order: TraverseOrder):
        if order == TraverseOrder.PRE_ORDER:
            self.tree_list.append(start_node.get_item())
        if start_node.get_left():
            self.traverse_node(start_node.get_left(), order)

        if order == TraverseOrder.IN_ORDER:
            self.tree_list.append(start_node.get_item())

        if start_node.get_right():
            self.traverse_node(start_node.get_right(), order)

        if order == TraverseOrder.POST_ORDER:
            self.tree_list.append(start_node.get_item())
