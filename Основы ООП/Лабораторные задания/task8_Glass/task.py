from typing import Union


#  создать класс Glass
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        # #  заменить на метод
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
        #   заменить на метод
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume):
        #   заменить на метод
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume <= 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем стакана

    def add_water_to_glass(self, water: Union[int, float]) -> None:
        if not isinstance(water, (int, float)):
            raise TypeError
        if water < 0:
            raise ValueError
        try_new_occupied_volume = self.occupied_volume + water
        if try_new_occupied_volume > self.capacity_volume:
            raise ValueError
        else: self.occupied_volume = try_new_occupied_volume

    def remove_water_from_glass(self, water: Union[int, float]) -> None:
        if not isinstance(water, (int, float)):
            raise TypeError
        if water < 0:
            raise ValueError
        try_new_occupied_volume = self.occupied_volume - water
        if try_new_occupied_volume < 0:
            raise ValueError
        else: self.occupied_volume = try_new_occupied_volume

    def __repr__(self) -> str:
        return f"Glass({self.capacity_volume}, {self.occupied_volume})"

    def __str__(self) -> str:
        return f"Стакан объёмом {self.capacity_volume}. Объём жидкости = {self.occupied_volume}"


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

    glass.add_water_to_glass(50)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.remove_water_from_glass(50)
    print(glass.capacity_volume, glass.occupied_volume)

    # glass.add_water_to_glass(150)
    # print(glass.capacity_volume, glass.occupied_volume)
    # glass.remove_water_from_glass(150)
    # print(glass.capacity_volume, glass.occupied_volume)
    #  Добавить методы add_water и remove_water