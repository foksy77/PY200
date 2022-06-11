from typing import Union


# TODO  создать класс Glass
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        # #  TODO заменить на метод
        # if not isinstance(capacity_volume, (int, float)):
        #     raise TypeError
        # if not capacity_volume > 0:
        #     raise ValueError
        # self.capacity_volume = capacity_volume  # объем стакана
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def init_capacity_volume(self, capacity_volume):
        #  TODO заменить на метод
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume):
        #  TODO заменить на метод
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume <= 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем стакана


    def __repr__(self) -> str:
        return f"Glass({self.capacity_volume}, {self.occupied_volume})"

    def __str__(self) -> str:
        return f"Стакан объёмом {self.capacity_volume}. Объём жидкости = {self.occupied_volume}"

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
