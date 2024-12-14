from dataclasses import dataclass

from gene.core.genealogy_person import GenealogyPerson
from gene.core.person import Person


@dataclass
class GenealogyBase:
    id: str
    person_list: list[Person]

    def __len__(self):
        return len(self.person_list)

    @property
    def person_idx(self):
        return {person.id: person for person in self.person_list}

    @property
    def genealogy_person_list(self):
        return [GenealogyPerson(self, person) for person in self.person_list]

    def __getitem__(self, key):
        person = self.person_idx[key]
        return GenealogyPerson(self, person)
