import pytest
import Tree
import Node


def create_tree(name: str = 'tree with no name'):
    root_item = 100
    n = Node.Node(root_item)
    t = Tree.Tree(n, name)
    right_items = (101, 102, 103, 300)
    left_items = (99, 98, 97, 2)
    all_items = left_items + right_items
    for item in all_items:
        t.add_node(item)
    return t


def test_tree_create():
    n = Node.Node(12)
    t = Tree.Tree(n)
    assert t.root == n


def test_add_new_item():
    t = create_tree('add_new_item')
    # add larger values
    assert t.add_node(104)
    assert t.add_node(1)


def test_add_existing_leaf_item():
    t = create_tree('add_existing_item')
    # add existing items fails
    assert not t.add_node(t.get_root_node().get_item())
    assert not t.add_node(300)
    assert not t.add_node(2)


def test_tree_search_last():
    n = Node.Node(0)
    t = Tree.Tree(n)
    search_item = 12
    for val in range(1, search_item + 1):
        assert t.add_node(val)
    assert t.search_item(search_item)


def test_tree_search_first():
    n = Node.Node(0)
    t = Tree.Tree(n)
    search_item = 1
    for val in range(1, 13):
        assert t.add_node(val)
    assert t.search_item(search_item)


def test_tree_search_not_found():
    n = Node.Node(0)
    t = Tree.Tree(n)
    search_item = 12
    for val in range(1, search_item + 1):
        assert t.add_node(val)
    assert not t.search_item(search_item + 1)


def test_traverse():
    # setup
    root_item = 100
    n = Node.Node(root_item)
    t = Tree.Tree(n, 'traverse')
    right_items = list(range(101, 110, 3))
    left_items = list(range(99, 89, -3))

    # add right, then left items
    for val in right_items + left_items:
        assert t.add_node(val)
    # assert
    t.traverse(Tree.TraverseOrder.PRE_ORDER)
    assert t.get_tree_list() == [root_item, ] + left_items + right_items


def test_get_height_root():
    # setup
    root_item = 100
    n = Node.Node(root_item)
    t = Tree.Tree(n, 'traverse')
    assert t.get_height() == 0


def test_get_height():
    # setup
    root_item = 100
    n = Node.Node(root_item)
    t = Tree.Tree(n, 'traverse')
    right_items = (101, 102, 103)
    left_items = (99, 98, 97, 2)
    all_items = left_items + right_items
    for item in all_items:
        t.add_node(item)

    assert t.get_height() == max(len(left_items), len(right_items))


def test_nodes_at_depth_0():
    t = create_tree()
    assert t.get_items_at_depth(t.get_root_node(), 0) == [100, ]


def test_nodes_at_depth_1():
    t = create_tree()
    assert t.get_items_at_depth(t.get_root_node(), 1) == [99, 101]


def test_nodes_at_depth_2():
    t = create_tree()
    assert t.get_items_at_depth(t.get_root_node(), 2) == [98, None, None, 102]


def test_nodes_at_depth_3():
    t = create_tree()
    assert t.get_items_at_depth(t.get_root_node(), 3) == [97, None, None, None, None, None, None, 103]


def test_nodes_at_depth_4():
    t = create_tree()
    filler = [None] * (pow(2, 4) - 2)
    exp_list = [2] + filler + [300]
    assert t.get_items_at_depth(t.get_root_node(), 4) == exp_list


def test_print_tree():
    t = create_tree()
    t.print_tree()
