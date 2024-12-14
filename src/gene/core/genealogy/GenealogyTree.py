class GenealogyTree:
    @property
    def root_list(self) -> list["GenealogyPerson"]:
        return [
            person for person in self.genealogy_person_list if person.is_root
        ]
