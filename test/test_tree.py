"""
test_tree
------------

Tests for `nekrobox.tree` module.
"""

import os
import shutil
import pytest

from nekrobox import tree


class TestConfigLoader():

    def test_path_walker(self):
        testtree = {"test": {"tree": 10}, "something": 5}
        assert tree.path_walker(testtree, "test tree".split()) == (10, [])
        assert tree.path_walker(testtree, "test tree something".split()) == (10, ["something"])
        assert tree.path_walker(testtree, "something tree".split()) == (5, ["tree"])
        with pytest.raises(KeyError):
            tree.path_walker(testtree, "nothing".split())

        with pytest.raises(KeyError):
            tree.path_walker(testtree, "test nothing".split())
