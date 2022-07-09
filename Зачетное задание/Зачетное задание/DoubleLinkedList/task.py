from collections.abc import MutableSequence
from typing import Any, Iterable, Optional
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    CLASS_NODE = Node
    def __init__(self, data: Iterable = None):
        """ Конструктор односвязного списка """
        self.len = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def is_valid(self, linkedlist: Any) -> None:
        if not isinstance(linkedlist, (type(None), LinkedList)):
            raise TypeError

    def insert(self, index: int, value: Any) -> None:
        ...

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            last_node = self.tail  # self.step_by_step_on_nodes(last_index)
            self.tail = append_node
            self.linked_nodes(last_node, append_node)
        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса и возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int):
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any):
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, key):
        ...

    def __len__(self):
        ...

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node


class DoubleLinkedList(LinkedList):
    CLASS_NODE = DoubleLinkedNode
    ...


if __name__ == "__main__":
    print("LinkedList ", "="*10)

    linkedlist_1 = LinkedList([1, 2, 3])
    linkedlist_2 = LinkedList([2, 3, 4])
    linkedlist_1.next = linkedlist_2
    print(linkedlist_1, linkedlist_2)
    # print(linkedlist_2)
    print(repr(linkedlist_1))
    print(repr(linkedlist_2))
