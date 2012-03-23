"""
generic API class for synkamatic
"""

class Synkamatic(object):
    paths = [] # paths in mozilla central
    github = None # github repository

    def __init__(self, github=None):
        self.github = github or self.gitub
        assert self.github, "github repository not specified!"
