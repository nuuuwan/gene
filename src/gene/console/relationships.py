LABELS = {
    0: {
        0: 'self',
        1: 'parent',
        2: 'grandparent',
        3: 'great-grandparent',
        4: 'great-great-grandparent',
        5: 'great-great-great-grandparent',
        6: 'great-great-great-great-grandparent',
        7: 'great-great-great-great-great-grandparent',
        -1: 'child',
        -2: 'grandchild',
        -3: 'great-grandchild',
        -4: 'great-great-grandchild',
        -5: 'great-great-great-grandchild',
        -6: 'great-great-great-great-grandchild',
        -7: 'great-great-great-great-great-grandchild',
    },
    1: {
        0: 'sibling',
        1: 'aunt/uncle',
        2: 'great-aunt/uncle',
        3: 'great-great-aunt/uncle',
        -1: 'niece/nephew',
        -2: 'great-niece/nephew',
        -3: 'great-great-niece/nephew',
    },
    2: {
        0: '1st cousin',
        1: '1st cousin once removed (aunt_uncle)',
        2: '1st cousin twice removed (great-aunt/uncle)',
        -1: '1st cousin once removed (niece/nephew)',
        -2: '1st cousin twice removed (great-niece/nephew)',
    },
}


def format_path(path):
    path_self, path_other = path.split(':')
    n_self, n_other = len(path_self), len(path_other)

    generation_gap = n_self - n_other
    common_ancestor_depth = min(n_self, n_other)

    default = f'r{generation_gap}-{common_ancestor_depth}'

    return LABELS.get(generation_gap, {}).get(common_ancestor_depth, default)
