"""
A collection of decorators for automatically decorating functions and methods
with sphinx documentation tags.
"""
import six
from six.moves import map


class DocParameters(object):
    """
    Automatically document parameters for a function or method.
    """

    def __init__(self, **argtypes):
        def _paramline(nametypedoc):
            """Takes (name, (type, doc)) converts to a param docstring line."""
            name, typedoc = nametypedoc
            return ":param {1} {0}: {2}".format(name, *typedoc)
        paramlines = map(_paramline, six.iteritems(argtypes))
        self.doc = '\n'.join(paramlines)

    def __call__(self, function):
        if function.__doc__:
            function.__doc__ = self.doc + function.__doc__
        else:
            function.__doc__ = self.doc
        return function
