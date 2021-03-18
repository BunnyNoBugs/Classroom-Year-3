class Coin:
    total_values_sum = 0

    def __init__(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self.value = value
        else:
            self.value = 0

        Coin.total_values_sum += self.value

    @classmethod
    def total_sum(cls) -> int:
        return cls.total_values_sum

    def __del__(self) -> None:
        Coin.total_values_sum -= self.value
