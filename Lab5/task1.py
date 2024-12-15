from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not (capacity_volume > 0):
            raise ValueError
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if (occupied_volume < 0):
            raise ValueError
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    # TODO инициализировать два объекта типа Glass
    glass1 = Glass(100, 100)
    glass2 = Glass(250, 75)
    # TODO попробовать инициализировать не корректные объекты
    glass3 = Glass(-100, 100)
    glass4 = Glass(250, -75)
    glass5 = Glass("750", 500)
