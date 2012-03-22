#!/usr/bin/env python

"""
doctest runner
"""

import doctest
import os
import sys
from optparse import OptionParser


def run_tests(raise_on_error=False, report_first=False):

    # add results here
    results = {}

    # doctest arguments
    directory = os.path.dirname(os.path.abspath(__file__))
    extraglobs = {'here': directory}
    doctest_args = dict(extraglobs=extraglobs, raise_on_error=raise_on_error)
    doctest_args['optionsflags'] = doctest.ELLIPSIS
    if report_first:
        doctest_args['optionflags'] |= doctest.REPORT_ONLY_FIRST_FAILURE

    # gather tests
    tests =  [test for test in os.listdir(directory)
              if test.endswith('.txt')]

    # run the tests
    for test in tests:
        try:
            results[test] = doctest.testfile(test, **doctest_args)
        except doctest.DocTestFailure, failure:
            raise
        except doctest.UnexpectedException, failure:
            raise failure.exc_info[0], failure.exc_info[1], failure.exc_info[2]

    return results

def main(args=sys.argv[1:]):

    # parse command line args
    parser = OptionParser(description=__doc__)
    parser.add_option('--raise', dest='raise_on_error',
                      default=False, action='store_true',
                      help="raise on first error")
    parser.add_option('--report-first', dest='report_first',
                      default=False, action='store_true',
                      help="report the first error only (all tests will still run)")
    options, args = parser.parse_args(args)

    # run the tests
    results = run_tests(**options.__dict__)
    if sum([i.failed for i in results.values()]):
        sys.exit(1) # error
                

if __name__ == '__main__':
    main()

