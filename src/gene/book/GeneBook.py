import os
from queue import Queue

from latex import (Chapter, Color, Italic, Items, Join, Label, LatexBook, Part,
                   Ref, Str, Texable)
from utils import Log

from gene.book.clusters import get_clusters
from gene.book.GenePersonLatex import COLOR_REF, GenePersonLatex
from gene.core.gene_dir.GeneDir import GeneDir

log = Log('GeneBook')
GENE_DIR = os.path.join('data', 'real-data', 'gene.20230828')
DESCENDENT_LIMIT = 30


class GeneBook(Texable):
    def __init__(self):
        self.label_set = set()
        self.gene = GeneDir.load(GENE_DIR)
        children = [LatexBook('Genealogy', 'Various Authors', *self.parts)]
        Texable.__init__(self, *children)

    @property
    def parts(self):
        for cluster_id in get_clusters(self.gene):
            root_person = self.gene[cluster_id]
            if self.get_spouse_label_if_exists(root_person):
                continue
            yield self.get_part(root_person)

    def get_part(self, root_person):
        log.debug('PART ' + root_person.full_name)
        chapters = self.get_chapters(root_person)
        return Part(GenePersonLatex(root_person).title_name, *chapters)

    def get_spouse_label_if_exists(self, current_person):
        for spouse in current_person.spouses:
            label = self.get_spouse_label(current_person.id, spouse.id)
            if label in self.label_set:
                return label
        return None

    def get_chapters(self, root_person):
        chapter_queue = Queue()
        chapter_queue.put(root_person)

        chapters = []
        while not chapter_queue.empty():
            current_person = chapter_queue.get()
            people_list, chapter = self.get_chapter(current_person)
            chapters.append(chapter)
            for people in people_list:
                chapter_queue.put(people)
        return chapters

    def get_chapter(self, person):
        person_list, content = self.get_root_person(person)
        return person_list, Chapter(
            GenePersonLatex(person).title_name, Label(person.id), content
        )

    def get_root_person(self, person):
        children = [GenePersonLatex(person).chapter_header]
        person_list, items = self.get_items(person)
        if items:
            children.append(Items(*items))
        children.append(GenePersonLatex(person).index_list)
        return person_list, Texable(*children)

    def get_leaf_person(self, person):
        if len(person.descendents) <= DESCENDENT_LIMIT:
            return self.get_inner_leaf_person(person)
        return self.get_chapter_leaf_person(person)

    def get_inner_leaf_person(self, person):
        children = [GenePersonLatex(person).full_name_in_order]
        person_list, items = self.get_items(person)
        if items:
            children.append(Items(*items))
        children.append(GenePersonLatex(person).index_list)
        return person_list, Texable(*children)

    def get_chapter_leaf_person(self, person):
        spouse_label = self.get_spouse_label_if_exists(person)
        if spouse_label:
            return [], GenePersonLatex(person).get_full_name_with_ref(
                spouse_label
            )
        return [person], GenePersonLatex(person).get_full_name_with_ref(None)

    def get_items(self, person):
        person_list = []
        items = []
        visited_child_ids = set()
        for spouse_id, child_ids in person.spouse_to_child_ids.items():
            (
                person_list2,
                items2,
                visited_child_ids,
            ) = self.get_spouse_children_item(
                person.id, spouse_id, child_ids, visited_child_ids
            )
            person_list.extend(person_list2)
            items.extend(items2)

        items = [item for item in items if item.tex.strip()]

        return person_list, items

    def get_spouse_label(self, person_id, spouse_id):
        spouse_ids = sorted([person_id, str(spouse_id)])
        return 'couple:' + ':'.join(spouse_ids)

    def get_spouse_children_item(
        self, person_id, spouse_id, child_ids, visited_child_ids
    ):
        spouse_person = self.gene[spouse_id] if spouse_id else None
        label = self.get_spouse_label(person_id, spouse_id)

        if label in self.label_set:
            return (
                [],
                [Color(COLOR_REF, Italic(Str('See '), Ref(label)))],
                visited_child_ids,
            )

        self.label_set.add(label)
        items = []

        inner_items = []
        person_list = []
        for child_id in child_ids:
            child_person = self.gene[child_id]
            child_person_list, content = self.get_leaf_person(child_person)
            person_list.extend(child_person_list)
            if content.tex.strip():
                inner_items.append(content)
            visited_child_ids.add(child_id)

        if inner_items:
            if spouse_id:
                items.append(
                    Join(
                        GenePersonLatex(spouse_person).as_spouse,
                        Str(' '),
                        Label(label),
                        Items(*inner_items),
                    )
                )
            else:
                items.extend(inner_items)
        elif spouse_id:
            items.append(Join()),
        return person_list, items, visited_child_ids
