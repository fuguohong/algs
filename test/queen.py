# coding=utf-8
import datetime


class NQueen:
    def __init__(self, n):
        self._n = n
        self._chessboard = []
        self._result = 0
        for i in range(n):
            self._chessboard.append([False] * n)

    def calculate(self):
        self._find(0)
        return self._result

    def _find(self, row):
        if row > 7:
            self._result += 1
            return
        for col in range(self._n):
            if self._check(row, col):
                self._chessboard[row][col] = True
                self._find(row + 1)
                self._chessboard[row][col] = False

    def _check(self, row, col):
        for check_row in range(self._n):
            if self._chessboard[check_row][col]:
                return False

        for check_row, check_col in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if self._chessboard[check_row][check_col]:
                return False

        for check_row, check_col in zip(range(row - 1, -1, -1), range(col + 1, self._n)):
            if self._chessboard[check_row][check_col]:
                return False

        return True


def calculate(n):
    calculater = NQueen(n)
    return calculater.calculate()


start_time = datetime.datetime.now()
result = calculate(16)
end_time = datetime.datetime.now()
print(result)
print('运行时长:', end_time - start_time)
