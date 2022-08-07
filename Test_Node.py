import pytest
import Node


def test_node_create():
    node_val = 180
    n = Node.Node(node_val)
    assert n
    assert not n.get_left()
    assert not n.get_right()
    assert n.get_item() == node_val
