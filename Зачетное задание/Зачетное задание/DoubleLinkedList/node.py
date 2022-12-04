from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка.
        :param value: Любое значение, которое помещено в узел.
        :param next_: следующий узел, если он есть.
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value}, {None})" \
            if self.next is None else f"{self.__class__.__name__}" \
            f"({self.value}, {self.__class__.__name__}({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """ Класс, который описывает узел многосвязного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev_: Optional["Node"] = None):
        """
        Создаем новый узел для многосвязного списка.
        :param value: Любое значение, которое помещено в узел.
        :param next_: следующий узел, если он есть.
        :param prev_: предыдущий узел, если он есть.
        """
        super().__init__(value, next_)
        self.prev = prev_  # вызовется setter

    def __repr__(self) -> str:
        next_repr: str = str(None) if self.next is None else \
            f"{self.__class__.__name__}({self.next.value}, {None}, {None})"
        prev_repr: str = str(None) if self.prev is None else \
            f"{self.__class__.__name__}({self.prev.value}, {None}, {None})"
        return f"{self.__class__.__name__}({self.value}, {next_repr}, {prev_repr})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DoubleLinkedNode"]):
        self.is_valid(prev_)
        self._prev = prev_

if __name__ == "__main__":
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)
    node_4 = Node(40)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    print(node_1.value)
    print(node_1)
    print(node_1.__repr__())


    first_node = DoubleLinkedNode(1)
    second_node = DoubleLinkedNode(2)
    third_node = DoubleLinkedNode(3)
    fourth_node = DoubleLinkedNode(4)

    first_node.next = second_node
    second_node.prev = first_node
    second_node.next = third_node
    third_node.prev = second_node
    third_node.next = fourth_node
    fourth_node.prev = third_node

    print(repr(first_node))
    print(repr(second_node))
    print(repr(third_node))
    print(repr(fourth_node))