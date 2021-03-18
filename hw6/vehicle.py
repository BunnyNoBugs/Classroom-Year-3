from abc import ABC, abstractmethod
import typing as tp


class Vehicle(ABC):
    def __init__(self, model: str = 'unknown') -> None:
        self.model = model

    @abstractmethod
    def move(self, distance: tp.Union[int, float]) -> None:
        pass


class Car(Vehicle):
    def move(self, distance: tp.Union[int, float]) -> None:
        if isinstance(distance, (int, float)) and distance >= 0:
            print(f'Автомобиль проехал {distance} километров')


class Boat(Vehicle):
    def move(self, distance: tp.Union[int, float]) -> None:
        if isinstance(distance, (int, float)) and distance >= 0:
            print(f'Лодка проплыла {distance} километров')
