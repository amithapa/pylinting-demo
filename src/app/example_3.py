from calendar import c
from typing import Union

class Person:
    def walk(self) -> None:
        print("Walking")

class Car:
    def drive(self) -> None:
        print("Driving")

MyObjects = Union[Person, Car]

def my_val(some: Car) -> None:
    some.drive()

def get_val(something: MyObjects) -> None:

    if not isinstance(something, Car):
        return
    for i in range(19):
        my_val(something)
    # something.walk()
    # if isinstance(something, Person):
    #     something.walk()
    # elif isinstance(something, Car):
    #     something.drive()


# pool: str

# def init():
#     global pool
#     pool = "amit"

# init()
# print(pool)
