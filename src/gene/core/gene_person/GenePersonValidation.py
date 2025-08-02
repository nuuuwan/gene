from fuzzywuzzy import fuzz

from gene.core.enums.PERSON import UNKNOWN_NAME


class GenePersonValidation:
    def similarity(self, other):
        if (
            UNKNOWN_NAME in self.full_name_in_order
            or UNKNOWN_NAME in other.full_name_in_order
        ):
            return 0
        return fuzz.ratio(self.full_name_in_order, other.full_name_in_order)

    def compare(self, other):
        print('')
        print(f'Comparing {self}')
        print(' ' * 4, f'with {other}')
        s = self.similarity(other)
        print('Name similarity', s)

        def check_conflict(label, func_var):
            self_var = func_var(self)
            other_var = func_var(other)
            if self_var and other_var:
                print('')
                print('CONFLICT', label)
                print(' ' * 4, self_var)
                print(' ' * 4, other_var)

        check_conflict('father', lambda x: x.father)
        check_conflict('mother', lambda x: x.mother)
        check_conflict('children', lambda x: x.children)
        check_conflict('spouses', lambda x: x.spouses)

        print('')
