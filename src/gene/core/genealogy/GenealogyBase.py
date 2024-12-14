from dataclasses import dataclass

from gene.core.person import Person


@dataclass
class GenealogyBase:
    id: str
    person_list: list[Person]

    def __len__(self):
        return len(self.person_list)
