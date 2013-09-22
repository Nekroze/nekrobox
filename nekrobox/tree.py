from .docdecs import params


@params(layers=(dict, "Dict tree of commands"),
        path=(list, "Path to walk down"),
        returns=(tuple, "The leaf and remainder of the path."))
def path_walker(layers, path):
    """Recursively walk the given path and return what is left.

    Walk through the given ``layers``, a dictionary tree, recursively until a
    `leaf` (anything that is not a dictionary) is found at which time it is
    returned along with any left over parts of the path.
    """
    head, tail = path[0], path[1:]
    branch = layers[head]
    if isinstance(branch, dict):
        return path_walker(branch, tail)
    else:
        return (branch, tail)
