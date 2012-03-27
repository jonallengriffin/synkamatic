"""
synkamatic front end for mozbase
https://github.com/mozilla/mozbase
"""

from api import Synkamatic

class Mozbase(Synkamatic):
    paths = ['testing/mozbase/'] # regex strings that represent paths in m-c
    github = 'https://github.com/mozilla/mozbase'


# for testing...
if __name__ == "__main__":
    synk = Mozbase()
    synk.start_pulse_listener()

