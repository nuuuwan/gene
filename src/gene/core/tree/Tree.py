import os
from dataclasses import asdict, dataclass

from utils import JSONFile, Log

from gene.core.person import Person

log = Log("Tree")


class TreeSerialize:
    @property
    def id_spaced(self):
        return self.id.replace(" ", "-")

    @property
    def json_path(self):
        return os.path.join("data", "trees", f"{self.id_spaced}.json")

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        JSONFile(self.json_path).write(self.to_dict())
        log.info(f"Wrote {len(self)} people to {self.json_path}")
        return self.json_path

    @classmethod
    def from_dict(cls, data):
        person_list = [Person(**person) for person in data["person_list"]]
        return Tree(data["id"], person_list)

    @classmethod
    def from_json(cls, json_path: str):
        tree = cls.from_dict(JSONFile(json_path).read())
        log.info(f"Read {len(tree)} people from {json_path}")
        return tree


@dataclass
class TreeBase:
    id: str
    person_list: list[Person]

    def __len__(self):
        return len(self.person_list)


class Tree(TreeBase, TreeSerialize):
    pass


if __name__ == "__main__":
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

    tree = Tree("Einstein Family", [p1, p2, p3])
    json_path = tree.to_json()
    tree2 = Tree.from_json(json_path)
    print("-" * 40)
    print(tree)
    print("-" * 40)
    print(tree2)
    print("-" * 40)
    assert tree == tree2
