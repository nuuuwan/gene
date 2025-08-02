from latex import Bold, Color, Index, Italic, Join, Ref, Str, Texable, escape

COLOR_REF = 'slteal'
COLOR_DETAILS = 'slmaroon'
COLOR_DATES = 'slorange'
COLOR_DATES_APPROX = 'gray'


class GenePersonLatex:
    def __init__(self, gene_person):
        self.gene_person = gene_person

    @property
    def title_name(self) -> str:
        return self.gene_person.full_name.replace('"', '')

    @property
    def chapter_header(self) -> Texable:
        return self.details

    @property
    def as_spouse(self) -> Texable:
        children = [
            Italic(Str('m.')),
            GenePersonLatex(self.gene_person).full_name_in_order,
        ]
        child_type = 'Son' if self.gene_person.is_male else 'Daughter'
        if self.gene_person.father:
            children.extend(
                [
                    Str(child_type + ' of '),
                    GenePersonLatex(
                        self.gene_person.father
                    ).full_name_with_ref,
                ]
            )

        if self.gene_person.mother:
            children.extend(
                [
                    Str(' \\& '),
                    GenePersonLatex(
                        self.gene_person.mother
                    ).full_name_with_ref,
                ]
            )

        return Join(*children)

    @property
    def details(self) -> Texable:
        return Color(
            COLOR_DETAILS, Italic(Str(escape(self.gene_person.details)))
        )

    @property
    def full_name(self) -> Texable:
        children = [
            Str(escape(self.gene_person.names)),
            Bold(Str(escape(self.gene_person.last_name))),
        ]

        return Join(*children)

    @property
    def full_name_in_order(self) -> Texable:
        dates_formatted = self.gene_person.dates_formatted
        color_dates = (
            COLOR_DATES_APPROX if ('?' in dates_formatted) else COLOR_DATES
        )
        children = [
            Str(escape(self.gene_person.names)),
            Bold(Str(escape(self.gene_person.last_name))),
            Color(color_dates, Italic(Str(dates_formatted))),
        ]
        if self.gene_person.details:
            children.append(self.details)

        return Join(*children)

    @property
    def full_name_with_ref(self) -> Texable:
        return self.get_full_name_with_ref(None)

    def get_full_name_with_ref(self, spouse_label) -> Texable:
        label = spouse_label or self.gene_person.id
        return Join(
            GenePersonLatex(self.gene_person).full_name_in_order,
            Color(
                COLOR_REF,
                Italic(
                    Str('See '),
                    Ref(label),
                ),
            ),
        )

    @property
    def index_list(self) -> Texable:
        children = []
        for name in self.gene_person.full_name_in_order.split(' '):
            if name.strip():
                children.append(Index(name))
        return Join(*children)
