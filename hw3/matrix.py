from sys import stdin
import copy
import typing as tp
import socket

HOST_NAME = 'DESKTOP-5JJVERA'


class MatrixError(Exception):
    def __init__(self, matrix1: 'Matrix', matrix2: 'Matrix') -> None:
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, elements: tp.List[tp.List[float]]) -> None:
        self._elements = copy.deepcopy(elements)

    def __str__(self) -> str:
        str_repr = ['\t'.join([str(z) for z in x]) for x in self._elements]
        str_repr = '\n'.join(str_repr)

        return str_repr

    def size(self) -> tuple:
        return len(self._elements), len(self._elements[0])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.size() != other.size():
            raise MatrixError(self, other)
        else:
            result = [[i + j for i, j in zip(x, y)] for x, y in zip(self._elements, other._elements)]
            result = Matrix(result)

        return result

    def __mul__(self, other: tp.Union[int, float, 'Matrix']) -> 'Matrix':
        if isinstance(other, (float, int)):
            result = [[i * other for i in x] for x in self._elements]
            result = Matrix(result)
        elif isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            else:
                other_transposed = Matrix.transposed(other)
                result = [[[l * m for l, m in zip(i, x)] for i in self._elements] for x in other_transposed._elements]
                result = [[sum(i) for i in x] for x in result]
                result = Matrix.transposed(Matrix(result))

        return result

    def __rmul__(self, other: tp.Union[int, float, 'Matrix']) -> 'Matrix':
        return self.__mul__(other)

    def transpose(self) -> 'Matrix':
        self._elements = [[i[x] for i in self._elements] for x in range(self.size()[1])]

        return self

    @staticmethod
    def transposed(matrix: 'Matrix') -> 'Matrix':
        result = copy.deepcopy(matrix)

        return result.transpose()


def main():
    if socket.gethostname() == HOST_NAME:  # для тестирования на локальном компьютере
        # Task 4 check 1
        mid = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
        m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
        print(mid * m1)
        print(mid * m2)
        print(m2 * m1)
        try:
            m = m1 * m2
            print("WA It should be error")
        except MatrixError as e:
            print(e.matrix1)
            print(e.matrix2)
    else:  # для тестирования на сервере
        exec(stdin.read())


if __name__ == '__main__':
    main()
