def dedupe(_list):
    assert isinstance(_list, list)
    return list(set(_list))


def list_map(self, _list, func):
    assert isinstance(_list, list)
    assert callable(func)
    return list(map(func, _list))


def list_filter(self, _list, func):
    assert isinstance(_list, list)
    assert callable(func)
    return list(filter(func, _list))
