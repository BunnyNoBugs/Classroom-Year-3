import socket

HOST_NAME = 'DESKTOP-5JJVERA'


class Money:
    def __init__(self, dollars: int, cents: int) -> None:
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self) -> int:
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value: int) -> None:
        if not (isinstance(value, int) and value >= 0):
            print('Error dollars')
        else:
            self.total_cents = self.total_cents % 100 + value * 100

    @property
    def cents(self) -> int:
        return self.total_cents % 100

    @cents.setter
    def cents(self, value: int) -> None:
        if not (isinstance(value, int) and 0 <= value < 100):
            print('Error cents')
        else:
            self.total_cents = self.total_cents // 100 * 100 + value

    def __str__(self) -> str:
        str_repr = f'Ваше состояние составляет ' \
                   f'{self.dollars} долларов {self.cents} центов'

        return str_repr


def main():
    if socket.gethostname() == HOST_NAME:
        bill = Money(101, 99)
        print(bill)
        bill.dollars = 666
        print(bill)
        bill.cents = 12
        print(bill)


if __name__ == '__main__':
    main()
