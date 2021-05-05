from abc import ABC, abstractmethod


class MyClothes(ABC):
    @abstractmethod
    def showCons(self):
        pass


class MySuit(MyClothes):
    def __init__(self, H: float):
        self.size = H
        self.name = 'костюм'

    @property
    def showCons(self):
        return f'Чтобы пошить {self.name} размером {self.size} общий расход ткани составит: {round(self.size / 6.5 + 0.5, 2)}'


class MyCoat(MyClothes):
    def __init__(self, V: float):
        self.size = V
        self.name = 'пальто'

    @property
    def showCons(self):
        return f'Чтобы пошить {self.name} размером {self.size} общий расход ткани составит: {round(2 * self.size + 0.3, 2)}'


try:
    coat = MyCoat(float(input('Введите размер для пальто: ')))
    suit = MySuit(float(input('Введите рост для костюма: ')))
except ValueError:
    exit('Параметр должен быть числом')

print(coat.showCons)
print(suit.showCons)
