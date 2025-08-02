from utils import Log

ID_ME = '00000018'

log = Log('clusters')


def are_descendents_valid(gene_person):
    return True
    descendent_ids = [
        descendent_info[0].id for descendent_info in gene_person.descendents
    ]
    return ID_ME in descendent_ids


def find_max_gene_person(gene, to_visit_set, descendents_set):
    max_n_descendants = 1
    max_gene_person = None
    max_descendents_set = None

    for person_id in sorted(to_visit_set):
        gene_person = gene[person_id]
        if not are_descendents_valid(gene_person):
            continue
        descendents = [x[0] for x in gene_person.descendents]
        new_descendents_set = set(descendents) - descendents_set

        n_descendants = len(new_descendents_set)
        if n_descendants > max_n_descendants:
            max_n_descendants = n_descendants
            max_gene_person = gene_person
            max_descendents_set = new_descendents_set

    if max_descendents_set:
        descendents_set.update(max_descendents_set)
        log.debug(
            f'max_gene_person: {max_gene_person.full_name} ({max_n_descendants:,})'
        )

    return max_gene_person, descendents_set


def update_descendents(max_gene_person, to_visit_set):
    for descendant_info in max_gene_person.descendents:
        person = descendant_info[0]
        if person.id in to_visit_set:
            to_visit_set.remove(person.id)
    return to_visit_set


def get_clusters(gene):
    to_visit_set = set(gene.person_index.keys())
    cluster_person_ids = []
    descendents_set = set()

    while to_visit_set:
        max_gene_person, descendents_set = find_max_gene_person(
            gene, to_visit_set, descendents_set
        )
        if not max_gene_person:
            break

        cluster_person_ids.append(max_gene_person.id)
        to_visit_set = update_descendents(max_gene_person, to_visit_set)

    return cluster_person_ids
