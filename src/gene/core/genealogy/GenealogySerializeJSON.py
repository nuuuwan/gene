import os
from dataclasses import asdict

from utils import JSONFile, Log

from gene.core.person import Person

log = Log("GenealogySerializeJSON")


class GenealogySerializeJSON:
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
        return cls(data["id"], person_list)

    @classmethod
    def from_json(cls, json_path: str):
        tree = cls.from_dict(JSONFile(json_path).read())
        log.info(f"Read {len(tree)} people from {json_path}")
        return tree
