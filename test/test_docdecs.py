#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_docdecs
------------

Tests for `nekrobox.docdecs` module.
"""
from nekrobox import docdecs


class TestNekrobox(object):
    def test_DocParameters(self):
        @docdecs.DocParameters(word=('str', 'echo this word'))
        def echo(word):
            return word

        assert echo.__doc__ == ":param str word: echo this word"
