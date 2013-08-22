#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_docdecs
------------

Tests for `nekrobox.docdecs` module.
"""
from nekrobox import docdecs


class TestNekrobox(object):
    def test_params(self):
        @docdecs.params(word=(str, 'echo this word'))
        def echo(word):
            return word

        @docdecs.params(input=(str, 'input to make lowercase'),
                        returns=(str, 'lowercase version of input'))
        def lowercase(text):
            return text.lower()

        assert echo.__doc__ == ":param str word: echo this word"
