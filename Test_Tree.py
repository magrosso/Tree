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
    start, delta = 100, 10
    n = Node.Node(start)
    t = Tree.Tree(n, 'traverse')

    larger_list = range(start + 1, start + delta)
    # add larger values in ascending order to the right
    for val in larger_list:
        n = Node.Node(val)
        assert t.add_node(n) == n

    smaller_list = range(start - 1, start - delta, -1)
    # add smaller values in descending order to the left
    for val in smaller_list:
        n = Node.Node(val)
        assert t.add_node(n) == n

    t.traverse()
    assert t.get_tree_list() == [start] + list(smaller_list) + list(larger_list)
