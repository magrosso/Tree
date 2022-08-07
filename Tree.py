from enum import Enum, auto
import Node


class TraverseOrder(Enum):
    PREORDER = auto()
    INORDER = auto()
    POSTORDER = auto()


# Binary search tree (BST)
class Tree:
    def __init__(self, root_node, name=''):
        self.root = root_node
        self.name = name

    def get_name(self):
        return self.name

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
                    #print(f'Added {new_node.get_item()} left of {next_node.get_item()}')
                    return new_node
            # insert right of parent
            elif new_node.get_item() > next_node.get_item():
                if next_node.get_right():
                    next_node = next_node.get_right()
                else:
                    # add new node to the right of next_node
                    next_node.set_right(new_node)
                    #print(f'Added {new_node.get_item()} right of {next_node.get_item()}')
                    return new_node
            else:
                # cannot insert node with existing value
                return None

    def traverse(self, start_node: Node = None) -> list:
        print(f'\nTree Traversal: {self.name}')
        next_node = start_node if start_node else self.root
        tree_list = [next_node.get_item()]
        while next_node:
            if next_node.get_left():
                next_node = next_node.get_left()
                tree_list.append(next_node.get_item())
            else:
                break

        next_node = start_node if start_node else self.root
        while next_node:
            if next_node.get_right():
                next_node = next_node.get_right()
                tree_list.append(next_node.get_item())
            else:
                break

        return tree_list

    def __str__(self):
        return str(self.root.get_item)
