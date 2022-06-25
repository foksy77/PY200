from task import DoubleLinkedNode


def double_linked_node_without_next_and_prev():
    middle_node = DoubleLinkedNode(2)

    expected_value = "DoubleLinkedNode(2, None, None)"
    actual_value = repr(middle_node)

    assert expected_value == actual_value


def double_linked_node_without_next():
    prev_node = DoubleLinkedNode(1)
    middle_node = DoubleLinkedNode(2)

    middle_node.prev = prev_node
    prev_node.next = middle_node

    expected_value = "DoubleLinkedNode(2, None, DoubleLinkedNode(1, None, None))"
    actual_value = repr(middle_node)

    assert expected_value == actual_value


def double_linked_node_init_prev():
    prev_node = DoubleLinkedNode(1)
    middle_node = DoubleLinkedNode(2, None, prev_=prev_node)
    prev_node.next = middle_node

    expected_value = "DoubleLinkedNode(2, None, DoubleLinkedNode(1, None, None))"
    actual_value = repr(middle_node)

    assert expected_value == actual_value


if __name__ == '__main__':
    double_linked_node_without_next_and_prev()
    double_linked_node_without_next()
    double_linked_node_init_prev()