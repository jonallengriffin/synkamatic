"""
synkamatic front end for mozbase
https://github.com/mozilla/mozbase
"""

from api import Synkamatic

class Mozbase(Synkamatic):
    paths = [] # TODO: paths in mozilla-central
    github = 'https://github.com/mozilla/mozbase'
