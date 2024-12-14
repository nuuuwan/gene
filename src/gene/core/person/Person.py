from dataclasses import dataclass

from utils import Log

log = Log("Person")


@dataclass
class Person:
    id: str
    name_list: list[str]
    gender: str
    date_of_birth: str
    date_of_death: str
    details_lines: list[str]
    father_id: str
    mother_id: str
    father_num: int
    mother_num: int
    spouse_id_list: list[str]

    def __str__(self):
        return " ".join(self.name_list)

    @property
    def is_female(self):
        return self.gender == "F"
