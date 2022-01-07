from random import randint
from typing import Union


class Calculator:
    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x + y

    def difference(
        self, x: Union[int, float], y: Union[int, float]
    ) -> Union[int, float]:
        return x - y

    def division(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x / y

    def hello(self) -> None:
        print("")
