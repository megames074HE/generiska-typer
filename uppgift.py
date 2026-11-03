from typing import TypeVar, Generic
T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

int_box = Box[int](10)

str_box = Box[str]("hej")

int_box.get_value()

str_box.get_value()

#Jo jag får förslag som ser ut såhär: -> int och -> str