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

    def print_row(self, items, row, height):
        """Arrange tree so that each parent appears centered above their two children
        """
        max_item_width = len('None') + 1
        item_width = max_item_width * pow(2, height - row)
        print()
        for item in items:
            print('{:^{width}}'.format(str(item), width=item_width), end='')

    def print_tree(self):
        print(f'\n{self.get_name()}')
        height = self.get_height()
        for row in range(height + 1):
            self.tree_list.clear()
            item_list = self.get_items_at_depth(self.root, row)
            self.print_row(item_list, row, height)

    def get_items_at_depth(self, node, depth):
        if depth == 0:
            self.tree_list.append(node.get_item())
            node = self.root
            return self.tree_list
        if node.get_left():
            self.get_items_at_depth(node.get_left(), depth - 1)
        else:
            self.tree_list.extend([None] * pow(2, depth - 1))
        if node.get_right():
            self.get_items_at_depth(node.get_right(), depth - 1)
        else:
            self.tree_list.extend([None] * pow(2, depth - 1))
        return self.tree_list

    def get_height(self) -> int:
        self.height = 0
        return self.get_node_height(self.root, 0)

    def get_node_height(self, node, height) -> int:
        left_height = self.get_node_height(node.get_left(), height + 1) if node.get_left() else height
        right_height = self.get_node_height(node.get_right(), height + 1) if node.get_right() else height
        return max(left_height, right_height)

    def search_item(self, item) -> bool:
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
                return True
        return False

    def add_node(self, new_item) -> bool:
        """
        :param new_item:
        :type new_item:
        :return: True if item added, False otherwise
        :rtype:
        """
        next_node = self.root
        while next_node:
            # insert left of parent
            if new_item < next_node.get_item():
                if next_node.get_left():
                    next_node = next_node.get_left()
                else:
                    # add new node to the left of next_node
                    next_node.set_left(Node.Node(new_item))
                    return True
            # insert right of parent
            elif new_item > next_node.get_item():
                if next_node.get_right():
                    next_node = next_node.get_right()
                else:
                    # add new node to the right of next_node
                    next_node.set_right(Node.Node(new_item))
                    return True
            else:
                return False

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
