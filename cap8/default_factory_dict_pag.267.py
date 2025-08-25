import collections


def make_multi_dict(items):
    dd = collections.defaultdict(list)
    for key, value in items:
        dd[key].append(value)
    return dd


mydd = make_multi_dict([(1,2), (1,3), (1,4), (1, 5), (3, 6)])
mydd[1]
