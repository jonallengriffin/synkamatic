"""
synkamatic front end for mozbase
https://github.com/mozilla/mozbase
"""

import sys
from api import Synkamatic

class Mozbase(Synkamatic):
    """
    Synkamatic class for Mozbase
    https://wiki.mozilla.org/Auto-tools/Projects/MozBase
    """

    paths = ['testing/mozbase/'] # regex strings that represent paths in m-c
    github = 'https://github.com/mozilla/mozbase'


def main(args=sys.argv[:]):
    synk = Mozbase()
    synk.start_pulse_listener()

if __name__ == "__main__":
    main()


