import pytest
import Tree
import Node


def test_tree_create():
    n = Node.Node(12)
    t = Tree.Tree(n)
    assert t.root == n


def test_add_new_node():
    start, delta = 100, 10
    n = Node.Node(start)
    t = Tree.Tree(n, 'add nodes')

    # add larger values to the right
    for val in range(start + 1, start + delta):
        n = Node.Node(val)
        assert t.add_node(n) == n
        f = t.search_node(val)
        assert f
        assert f.get_item() == val

    # add smaller values to the left
    for val in range(start - 1, start - delta, -1):
        n = Node.Node(val)
        assert t.add_node(n) == n
        f = t.search_node(val)
        assert f
        assert f.get_item() == val
    # assert t.traverse() == list(range(start - delta, start + delta))


def test_tree_search_last():
    n = Node.Node(0)
    t = Tree.Tree(n)
    search_item = 12
    for val in range(1, search_item + 1):
        n = Node.Node(val)
        assert t.add_node(n) == n
    f = t.search_node(search_item)
    assert f
    assert f.get_item() == search_item


def test_tree_search_first():
    n = Node.Node(0)
    t = Tree.Tree(n)
    search_item = 1
    for val in range(1, 13):
        n = Node.Node(val)
        assert t.add_node(n) == n
    f = t.search_node(search_item)
    assert f
    assert f.get_item() == search_item


def test_tree_search_not_found():
    n = Node.Node(0)
    t = Tree.Tree(n)
    search_item = 12
    for val in range(1, search_item + 1):
        n = Node.Node(val)
        assert t.add_node(n) == n
    f = t.search_node(search_item + 1)
    assert not f


def test_traverse():
    # setup
    root_item = 100
    n = Node.Node(root_item)
    t = Tree.Tree(n, 'traverse')
    right_items = list(range(101, 110, 3))
    left_items = list(range(99, 89, -3))

    # add right, then left items
    for val in right_items + left_items:
        n = Node.Node(val)
        assert t.add_node(n) == n
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
        node = Node.Node(item)
        t.add_node(node)

    assert t.get_height() == max(len(left_items), len(right_items))
