from dataclasses import dataclass

from utils import Log

log = Log("Person")


@dataclass
class Person:
    id: str
    names: list[str]
    date_of_birth: str
    date_of_death: str
    detail_lines: list[str]
    father_id: str
    mother_id: str
    father_num: int
    mother_num: int

    def __str__(self):
        return " ".join(self.names)
