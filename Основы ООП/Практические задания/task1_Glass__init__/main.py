from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume <= 0:
            raise ValueError
        self.occupied_volume = occupied_volume


if __name__ == "__main__":

    glass1 = Glass(200, 100)
    print(glass1.capacity_volume, glass1.capacity_volume)

    glass2 = Glass(500, 100)
    print(glass2.capacity_volume, glass2.capacity_volume)



    glass3 = Glass(500, -100)
