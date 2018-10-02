import dataclasses
from enum import IntEnum
from typing import List


class Label(IntEnum):
    POSITIVE = 1
    NEGATIVE = -1


@dataclasses.dataclass(frozen=True)
class Feature:
    index: int
    value: float


@dataclasses.dataclass(frozen=True)
class Data:
    features: List[Feature]
    label: Label
