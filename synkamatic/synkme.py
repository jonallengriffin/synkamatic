"""
synkamatic front end for synkme (a test repository)
https://github.com/jonallengriffin/synkme
"""

import sys
from api import Synkamatic

class Synkme(Synkamatic):
    """
    Synkamatic class for Synkme
    """

    paths = ['README'] # paths in hg
    github = 'https://github.com/jonallengriffin/synkme'


def main(args=sys.argv[:]):
    synk = Synkme()
    synk.start_pulse_listener()

if __name__ == "__main__":
    main()


