"""
A collection of decorators for automatically decorating functions and methods
with sphinx documentation tags.
"""
import six
from six.moves import map


def params(**argtypes):
    """
    A decorator that automatically adds parameter and return type tags to a
    function or method docstring.

    Input should be specified as the parameter keyword/name and then a tuple of
    its type and a description string. This will also use the `returns` keyword
    to identify the returned type and documentation. The following is an
    example of how to use `docparams` to automatically document arguments::

        @docparams(input=(str, "string to be made lowercase.")
                   returns=(str, "lowercase string"))
        def lowercase(input):
            return input.lower()
    """
    def modify(function):
        def paramline(nametypedoc):
            """Takes (name, (type, doc)) converts to a param docstring line."""
            name, (atype, doc) = nametypedoc
            return ":param {1} {0}: {2}".format(name, atype.__name__, doc)

        rtype, rdoc = argtypes.pop("returns", (None, None))
        paramlines = list(map(paramline, six.iteritems(argtypes)))

        if rdoc:
            paramlines.append(":return: {0}".format(rdoc))
        if rtype:
            paramlines.append(":rtype: {0}".format(rtype))

        doc = '\n'.join(paramlines)

        if function.__doc__:
            function.__doc__ = doc + function.__doc__
        else:
            function.__doc__ = doc
        return function
    return modify
