from random import randint

class Matrix:
    def __init__(self, items: list):
        self.items = items

    def __str__(self):
        printMatrix = ''
        for item in self.items:
            matrixPrint = " ".join(map(str, item))
            printMatrix += matrixPrint + '\n'
        return printMatrix

    def __add__(self, other):
        if len(self.items) != len(other.items):
            return f'Складывать и вычитать можно матрицы одного размера!'
        else:
            sumMatrix = []
            for i in range(len(self.items)):
                matrixRow = []
                for j in range(len(self.items[i])):
                    matrixRow.append(self.items[i][j] + other.items[i][j])
                sumMatrix.append(matrixRow)
            return Matrix(sumMatrix)


def generateMatrix(row: int, col: int):
    generateMatrix = []
    for i in range(row):
        matrixRow = []
        for j in range(col):
            matrixRow.append(randint(-5, 5))
        generateMatrix.append(matrixRow)
    return generateMatrix


print('Элементы матриц будем генерировать')
try:
    userRow = int(input('Введите количество строк в матрицах для сложения: '))
    userCol = int(input('Введите количество столбцов в матрицах для сложения: '))
except ValueError:
    exit('Вводить можно только целые числа')
matrixA = Matrix(generateMatrix(userRow, userCol))
matrixB = Matrix(generateMatrix(userRow, userCol))

print(f'\nПервая матрица:\n{matrixA}')
print(f'Вторая матрица:\n{matrixB}')
print(f'Сумма матриц:\n{matrixA + matrixB}')
print(f'Вывод произвольной сгенерированной матрицы:\n{Matrix(generateMatrix(randint(2, 7), randint(2, 7)))}')
