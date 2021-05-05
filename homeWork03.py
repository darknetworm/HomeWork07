class Cell:
    def __init__(self, unitOfCell: int):
        self.unitOfCell = unitOfCell

    def __add__(self, other):
        return f'При объединении клеток {self.unitOfCell} и {other.unitOfCell} число ячеек будет {self.unitOfCell + other.unitOfCell}'

    def __sub__(self, other):
        subCell = self.unitOfCell - other.unitOfCell
        if subCell < 0:
            return f'Невозможно вычесть из меньшей клетки {self.unitOfCell} большую {other.unitOfCell}'
        else:
            return f'При вычитании клеток {self.unitOfCell} и {other.unitOfCell} число ячеек будет {subCell}'

    def __mul__(self, other):
        return f'При умножении клеток {self.unitOfCell} и {other.unitOfCell} число ячеек будет {self.unitOfCell * other.unitOfCell}'

    def __truediv__(self, other):
        return f'При делении клеток {self.unitOfCell} и {other.unitOfCell} число ячеек будет {self.unitOfCell // other.unitOfCell} с округлением в меньшую сторону'

    def make_order(self, unitInRow: int):
        self.unitInRow = unitInRow
        strToReturn = ''

        for i in range(0, int(self.unitOfCell / self.unitInRow)):
            # tmpStr = ('*' * self.unitInRow) + '\n'
            strToReturn = strToReturn + ('*' * self.unitInRow) + '\n'
        if self.unitOfCell % self.unitInRow != 0:
            strToReturn = strToReturn + ('*' * (self.unitOfCell % self.unitInRow)) + '\n'
        return (f'Распределение {self.unitOfCell} ячеек по {self.unitInRow} рядам:\n{strToReturn[0:-1]}')


cellOne = Cell(6)
cellTwo = Cell(4)
cellThree = Cell(12)
cellFour = Cell(15)

print(cellOne + cellTwo)
print(cellOne - cellTwo)
print(cellOne * cellTwo)
print(cellOne / cellTwo)
print(cellThree.make_order(5))
print(cellFour.make_order(5))
