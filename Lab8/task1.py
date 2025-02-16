class Car:
    """
    Базовый класс Автомобиль
    """
    
    def __init__(self, brand: str, model: str, year: int, fuel_type: str, horsepower: int, load_capacity: int):
        """
        Конструктор класса

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param fuel_type: Тип топлива
        :param horsepower: Кол-во л.с
        :param load_capacity: Грузоподъёмность

        Примеры:
        >>> car_1 = Car("Toyota", "Vitz", 2024, "бензин", 95, 275)
        >>> car_2 = Car("Tesla", "Cybertrack", 2023, "электричество", 600, 1400)
        >>> car_3 = Car("Kia", "Sorento", 2025, "гибрид", 200, 680)
        """
        self.validate_attributes(brand, model, year, fuel_type, horsepower, load_capacity)
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.horsepower = horsepower
        self.load_capacity = load_capacity

    def validate_attributes(self, brand: str, model: str, year: int, fuel_type: str, horsepower: int, load_capacity: int):
        """
        Валидация входных данных

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param fuel_type: Тип топлива
        :param horsepower: Кол-во л.с
        :param load_capacity: Грузоподъёмность
        """
        if not isinstance(brand, str):
            raise TypeError('Название марки должно быть строкового типа.')
        if not isinstance(model, str):
            raise TypeError('Названи модели должно быть строкового типа.')
        if not isinstance(year, int):
            raise TypeError('Год выпуска должен быть целочисленного типа.')
        if not isinstance(fuel_type, str):
            raise TypeError('Вид топлива должен быть строкового типа.')
        if not isinstance(horsepower, int):
            raise TypeError('Кол-во лошадинных сил должно быть целочисленного типа.')
        if not isinstance(load_capacity, int):
            raise TypeError('Грузоподъемность должна быть целочисленного типа.')
        if horsepower <= 0:
            raise ValueError('Кол-во лошадиных сил должно быть положительным числом.')
        if load_capacity <= 0:
            raise ValueError('Грузоподъёмность должна быть положительным числом.')
    
    def __str__(self) -> str:
        """
        Магический метод для представления объекта в виде строки

        :return: Строковое представление объекта
        """
        return f"Автомобиль: {self.brand} {self.model} ({self.year}), топливо: {self.fuel_type}, кол-во л.с: {self.horsepower}, грузоподъемность: {self.load_capacity}"
    
    def __repr__(self) -> str:
        """
        Магический метод для получения 'читаемого' представления объекта в виде строки для отладки

        :return: Строковое представление объекта
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, fuel_type={self.fuel_type!r}, horsepower={self.horsepower!r}, load_capacity={self.load_capacity})"

    def is_electric(self) -> bool:
        """
        Определение является ли автомобиль электрическим

        :return: Булевое значение

        Пример:
        >>> car_1.is_electric()
        """
        return self.fuel_type.lower() in {"электричество", "гибрид"}

    def insurance_cost(self) -> float:
        """
        Расчёт стоимости страхования
        Данный метод перегружен в дочерних классах

        :return: Стоимость страхования

        Пример:
        >>> car_1.insurance_cost()
        """
        base_cost = 6000
        return base_cost + (self.horsepower * 10) + (self.load_capacity * 0.5)


class LightCar(Car):
    """
    Дочерний класс Легковой Автомобиль, наследуемый от базового класса Car.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str, horsepower: int, load_capacity: int, seats: int):
        """
        Конструктор класса

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param fuel_type: Тип топлива
        :param horsepower: Кол-во л.с
        :param load_capacity: Грузоподъёмность
        :param seats: Количество мест

        Пример:
        >>> light_car_1 = LightCar('Toyota', 'Vitz', 2024, 'бензин', 95, 275, 5)
        """
        super().__init__(brand, model, year, fuel_type, horsepower, load_capacity)
        self.validate_seats(seats)
        self.seats = seats

    def validate_seats(self, seats: int):
        """
        Валидация количества мест в автомобиле.

        :param seats: Количество мест
        """
        if not isinstance(seats, int):
            raise TypeError("Количество мест должно быть целочисленного типа.")
        if seats <= 0:
            raise ValueError("Количество мест должно быть положительным числом.")

    def __str__(self) -> str:
        """
        Магический метод для представления объекта в виде строки
        """
        return f"Легковой автомобиль: {self.brand} {self.model} ({self.year}), топливо: {self.fuel_type}, л.с: {self.horsepower}, грузоподъемность: {self.load_capacity}, кол-во мест: {self.seats}"

    def __repr__(self) -> str:
        """
        Магический метод для получения строкового представления объекта для отладки.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, fuel_type={self.fuel_type!r}, horsepower={self.horsepower!r}, load_capacity={self.load_capacity!r}, seats={self.seats!r})"

    def is_family_car(self) -> bool:
        """
        Определение является ли автомобиль подходящим для семьи

        :return: Булевое значение

        Пример:
        >>> light_car_1.is_family_car()
        """
        return self.seats >= 5

    def insurance_cost(self) -> float:
        """
        Расчёт стоимости страхования
        Метод перегружен с учётом того, что стоимость страхования легковых машин меньше стоимости страхования грузовых

        :return: Стоимость страхования

        Пример:
        >>> light_car_1.insurance_cost()
        """
        base_cost = 4000
        return base_cost + (self.horsepower * 10) + (self.load_capacity * 0.5)


class TruckCar(Car):
    """
    Дочерний класс Грузовой автомобиль, наследуемый от базового класса Car.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str, horsepower: int, load_capacity: int, cargo_weight: int):
        """
        Конструктор класса

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param fuel_type: Тип топлива
        :param horsepower: Кол-во л.с
        :param load_capacity: Грузоподъёмность
        :param cargo_weight: Вес груза

        Пример:
        >>> truck_car_1 = TruckCar('КАМАЗ', 'Компас 9', 2022, "дизель", 150, 6250, 500)
        """
        super().__init__(brand, model, year, fuel_type, horsepower, load_capacity)
        self.validate_cargo_weight(cargo_weight)
        self.cargo_weight = cargo_weight

    def validate_cargo_weight(self, cargo_weight: int):
        """
        Валидация веса груза в автомобиле. 

        :param cargo_weight: Вес груза
        """
        if not isinstance(cargo_weight, int):
            raise TypeError("Вес груза должен быть целочисленного типа.")
        if cargo_weight < 0:
            raise ValueError("Вес груза не может быть отрицательным числом.")
    
    def __str__(self) -> str:
        """
        Магический метод для представления объекта в виде строки
        """
        return f"Грузовой автомобиль: {self.brand} {self.model} ({self.year}), топливо: {self.fuel_type}, л.с: {self.horsepower}, грузоподъемность: {self.load_capacity}, вес груза: {self.cargo_weight}"

    def __repr__(self) -> str:
        """
        Магический метод для получения строкового представления объекта для отладки.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, fuel_type={self.fuel_type!r}, horsepower={self.horsepower!r}, load_capacity={self.load_capacity!r}, cargo_weight={self.cargo_weight!r})"

    def can_carry(self, weight: int) -> bool:
        """
        Определение способен ли грузовик переносить заданный вес

        :return: Булевое значение

        Пример:
        >>> car_1.can_carry(100)
        """
        return weight <= self.load_capacity

    def insurance_cost(self) -> float:
        """
        Расчёт стоимости страхования
        Метод перегружен с учётом того, что стоимость страхования грузовых машин выше стоимости страхования легковых

        :return: Стоимость страхования

        Пример:
        >>> truck_car_1.insurance_cost()
        """
        base_cost = 8000
        return base_cost + (self.horsepower * 10) + (self.load_capacity * 0.5)


if __name__ == "__main__":
    pass
