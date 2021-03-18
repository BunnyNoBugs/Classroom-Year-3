import typing as tp
import socket

HOST_NAME = 'DESKTOP-5JJVERA'


class GoodInt(int):
    def __new__(cls, x: tp.Union[int, float, str]) -> int:  # pylint сообщает,
        # что "Value 'tp.Union' is unsubscriptable", но, похоже,
        # это ложное срабатывание: https://github.com/PyCQA/pylint/issues/3882
        return int.__new__(cls, round(float(x)))


def main():
    if socket.gethostname() == HOST_NAME:
        value = '5.5'
        good_int = GoodInt(value)
        print(value)
        print(good_int)


if __name__ == '__main__':
    main()
