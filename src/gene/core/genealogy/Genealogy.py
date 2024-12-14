from utils import Log

from gene.core.genealogy.GenealogyBase import GenealogyBase
from gene.core.genealogy.GenealogySerializeJSON import GenealogySerializeJSON
from gene.core.genealogy.GenealogyTree import GenealogyTree

log = Log("Genealogy")


class Genealogy(GenealogyBase, GenealogySerializeJSON, GenealogyTree):
    pass


if __name__ == "__main__":
    from gene.core.person import Person

    p1 = Person(
        "1",
        ["Albert", "Einstein"],
        "1901-03-14",
        "1954-04-18",
        ["Born in Germany", "Died in USA"],
        "2",
        "3",
        1,
        1,
    )
    p2 = Person(
        "2",
        ["Hermann", "Einstein"],
        "1847-08-30",
        "1902-10-10",
        ["Born in Germany", "Died in Italy"],
        None,
        None,
        None,
        None,
    )

    p3 = Person(
        "3",
        ["Pauline", "Koch"],
        "1858-02-08",
        "1920-02-20",
        ["Born in Germany", "Died in Germany"],
        None,
        None,
        None,
        None,
    )

    g = Genealogy("Einstein Family", [p1, p2, p3])
    json_path = g.to_json()
    g2 = Genealogy.from_json(json_path)
    print("-" * 40)
    print(g)
    print("-" * 40)
    print(g2)
    assert g == g2

    print("-" * 40)
    print([str(person) for person in g.root_list])
