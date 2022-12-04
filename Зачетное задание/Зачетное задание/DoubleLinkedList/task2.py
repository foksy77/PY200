from collections.abc import MutableSequence
from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """ Конструктор односвязного списка.
        :param data: Iterable.
        """
        self.len = 0
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None
        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)  # при таком раскладе надо перегрузить в DoubleLinkedList
        # append_node = self.CLASS_NODE(value)  # при таком раскладе наследуем в DoubleLinkedList
        if self.head is None:
            self.head = self.tail = append_node
        else:
            last_node = self.tail  # self.step_by_step_on_nodes(last_index)
            self.tail = append_node
            self.linked_nodes(last_node, append_node)
        self.len += 1

    def insert(self, index: int, value: Any) -> None:  # fix me реализовать
        """ Вставка узла по указанному индексу.
        :param index: Индекс элемента для вставки.
        :param value: Значение узла.
        """
        insert_node = Node(value)
        if index > self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)
            self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:  # -> CLASS_NODE:
        """ Метод выполняет перемещение по узлам до указанного индекса и возвращает узел. """
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int) -> Any:
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index) -> None:  # fix me реализовать
        """ Удаление узла по индексу. """
        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self.len -= 1

    def __len__(self) -> int:
        return self.len

    # def remove(self, value) -> None:  # fixme добавить ValueError
    #     """ Удаление узла по значению узла. """
    #     for i in range(self.len):
    #         if self.__getitem__(i) == value:
    #             self.__delitem__(i)
    #             break

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({[i for i in self]})"  # {self.__class__.__name__}

    def __str__(self) -> str:
        # return f"{self.to_list()}"
        return f"{[i for i in self]}"

    @staticmethod
    # def linked_nodes(left_node: CLASS_NODE, right_node: Optional[CLASS_NODE] = None) -> None:
    def linked_nodes(left_node: Node, right_node: Optional["Node"] = None) -> None:
        """
        Функция связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        # if CLASS_NODE == DoubleLinkedNode:
        #     right_node.prev = left_node



class DoubleLinkedList(LinkedList):
    ...

if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4, 5])
    print(ll)