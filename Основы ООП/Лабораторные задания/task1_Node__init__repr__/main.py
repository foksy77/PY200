from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """

        self.value = value
        self.next_ = next_


    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return self.value

    def get_next(self) -> Optional["Node"]:
        """Метод, который возвращает значение атрибута value"""
        return self.next_

        # инициализировать атрибуты экземпляра класса Node
        ...

    def __repr__(self) -> str:
        return f"Node({self.get_value()}, {self.get_next()})"

    # def __str__(self) -> str:
    #     return f"Стакан объёмом {self.capacity_volume}. Объём жидкости = {self.occupied_volume}"


if __name__ == '__main__':
    first_node = Node(1)  #  инициализировать первый узел

    second_node = Node(2)  #  инициализировать второй узел
    first_node.next_ = second_node

    print(first_node)
    print(second_node)
