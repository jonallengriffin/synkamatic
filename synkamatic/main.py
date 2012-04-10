#!/usr/bin/env python

"""
Synkamatic helps to automate the syncing of changes between mirrored Mozilla hg and github repos
"""

# Things we'll need:
# - a github account to turn hg pulled events into pull requests
# - pulse monitoring of hg commits to mozilla-central

import sys
import optparse

from mozbase import Mozbase

# dictionary of Synkamatic classes
synks = {
    'mozbase': Mozbase,
}

def main(args=sys.argv[:]):

    # parse command line options
    usage = '%prog [options]'
    class PlainDescriptionFormatter(optparse.IndentedHelpFormatter):
        """description formatter for console script entry point"""
        def format_description(self, description):
            if description:
                return description + '\n'
            else:
                return ''
    parser = optparse.OptionParser(usage=usage, description=__doc__, formatter=PlainDescriptionFormatter())

    parser.add_option("--pulsefile", action="store",
                      type="string", dest="pulsefile", default=None,
                      help="path to file containing a pulse message (in JSON "
                      "format) to be injected into the pulse listener for testing")

    parser.add_option("--synk", action="store",
                      type="string", dest="synk", default="mozbase",
                      help="the synkamatic to execute")

    options, args = parser.parse_args(args)

    synk = synks.get(options.synk, Mozbase)(pulsefile=options.pulsefile)
    synk.start_pulse_listener()


if __name__ == '__main__':
    main()
