def sort_dict_by_key(d):
    return dict(
        sorted(
            d.items(),
            key=lambda item: item[0],
        )
    )
