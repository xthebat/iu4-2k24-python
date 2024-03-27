import math
from dataclasses import dataclass
from io import StringIO
from typing import Optional, TextIO

import pytest


class Animal:

    def __init__(self, name: str, kind: str = None):
        self.name: str = name  # public
        self._kind: str = kind  # protected
        self.__count: Optional[int] = 1  # private
        self._list_field: list[int] = [1, 2, 3]

    def get_kind(self) -> str:
        return self._kind

    def get_count(self) -> Optional[int]:
        return self.__count

    def get_list_field(self):
        return self._list_field

    @property
    def count(self):
        return self.__count

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value: str):
        self._kind = value

    def say(self, where: TextIO = None):
        raise NotImplementedError

    def add_count(self, count: int = 1):
        self.__count += count


class Cat(Animal):

    def __init__(self, name: str):
        super().__init__(name, "Cat")

    def say(self, where: TextIO = None):
        print("MEOW", file=where)

    def add_count(self, count: int = 1):
        super().add_count(2 * count)

    def __str__(self):
        return f"Cat[name={self.name}]"

    def __repr__(self):
        # return self.__str__()
        return str(self)


def test_animal_str():
    animal = Animal("Tom", "Cat")
    print(animal)

    cat = Cat("Tom")
    print(cat)

    cats_list = [Cat("Tom"), Cat("XXX"), Cat("YYY")]
    print(cats_list)


def test_animal_fields_invalid():
    animal = Animal("Tom", "Cat")
    assert animal.name == "Tom"
    assert animal._kind == "Cat"  # dont do this!!!
    assert animal._Animal__count == 1  # and that


def test_animal_fields_with_getter():
    animal = Animal("Tom", "Cat")
    animal.name = "Bobik"
    assert animal.name == "Bobik"

    assert animal.get_kind() == "Cat"
    assert animal.get_count() == 1

    list_field = animal.get_list_field()
    list_field.append(100)

    assert animal._list_field == [1, 2, 3, 100]


def test_animal_fields_with_property():
    animal = Animal("Tom", "Cat")
    assert animal.kind == "Cat"
    animal.kind = "Dog"
    assert animal._kind == "Dog"


def test_inheritance():
    animal = Animal("Tom", "Cat")
    print(animal)

    with pytest.raises(NotImplementedError):
        animal.say()

    cat = Cat("Tom")
    cat.add_count(100)

    stream = StringIO()

    assert cat.get_count() == 201
    cat.say(stream)
    stream.seek(0)
    data = stream.read()
    assert data == "MEOW\n"


@dataclass
class Vector:
    x: float
    y: float
    z: float

    def square_length(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self):
        return math.sqrt(self.square_length())

    @classmethod
    def from_text(cls, text: str):
        tokens = [it.strip() for it in text.split()]
        if len(tokens) != 3:
            raise ValueError(f"Invalid tokens count for {text=}")

        try:
            values = [float(it) for it in tokens]
        except ValueError:
            raise ValueError(f"Can't create vector from {text=}")

        return cls(*values)

    def to_text(self):
        return f"{self.x:.3f} {self.y:.3f} {self.z:.3f}"

    def to_stream(self, stream: TextIO):
        raise NotImplementedError("IMPLEMENT ME")

    @classmethod
    def create0(cls, text: str = None, stream: TextIO = None):
        if text is not None:
            ...
        elif stream is not None:
            ...

    @classmethod
    def create1(cls, source):
        if isinstance(source, str):
            ...
        elif isinstance(source, StringIO):
            ...

    @staticmethod
    def from_stream(stream: TextIO):
        raise NotImplementedError("NEVER BE IMPLEMENTED")


@dataclass
class CoolVector(Vector):

    def sum(self):
        return self.x + self.y + self.z


@dataclass
class Rotator:
    pitch: float
    yaw: float
    roll: float


@dataclass
class Node:
    position: Vector
    rotation: Rotator


def test_vector():
    v = Vector(1.0, 2.0, 3.0)
    assert v.square_length() == 14.0


def test_classmethod():
    v = Vector.from_text("1.0 2.0 3.0")
    assert isinstance(v, Vector)
    assert v.square_length() == 14.0

    cv = CoolVector.from_text("1.0 2.0 3.0")
    assert isinstance(cv, CoolVector)
    assert cv.square_length() == 14.0
    assert cv.sum() == 6.0
    print(cv)

    cv.x = 10.0
    cv.y = 10.0

    assert cv.square_length() == 209.0
    assert cv.to_text() == "10.000 10.000 3.000"

