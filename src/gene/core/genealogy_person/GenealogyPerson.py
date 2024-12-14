from gene.core.person import Person


class GenealogyPerson(Person):
    def __init__(
        self,
        genealogy,
        person,
    ):
        super().__init__(**person.__dict__)
        self.genealogy = genealogy

    @property
    def first_spouse(self):
        return (
            self.genealogy[self.spouse_id_list[0]]
            if len(self.spouse_id_list) > 0
            else None
        )

    @property
    def has_father(self):
        return self.father_id is not None

    @property
    def has_mother(self):
        return self.mother_id is not None

    @property
    def has_spouse(self):
        return len(self.spouse_id_list) > 0

    @property
    def has_wife(self):
        return self.first_spouse and self.first_spouse.is_female

    @property
    def is_root(self):
        return (
            not self.has_father
            and not self.has_mother
            and (not self.has_spouse or (self.has_wife))
        )
