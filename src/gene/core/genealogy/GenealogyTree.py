from gene.core.person import Person


class GenealogyTree:
    @property
    def root_list(self) -> list[Person]:
        return [
            person
            for person in self.person_list
            if person.father_id is None and person.mother_id is None
        ]
