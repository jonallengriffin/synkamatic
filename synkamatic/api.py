"""
generic API class for synkamatic
"""
from mozillapulse.consumers import CodeConsumer
import re
import socket
import sys


class Synkamatic(object):
    """
    sync mozilla repositories <-> github
    using pulse messages for communication and
    bugzilla and github pull-requests as
    human-moderatable media
    """

    paths = [] # a list of regex's to match against paths in hg
    github = None # github repository
    bugzilla = 'https://api-dev.bugzilla.mozilla.org/latest/' # REST API for bugzilla
    reviewer = None # reviewer for github -> bugzilla patches
    cc = [] # bugzilla users to CC for github -> bugzilla patches

    def __init__(self, github=None, paths=None, tree='mozilla-central'):
        self.github = github or self.github
        assert self.github, "github repository not specified!"
        filepaths = paths or self.paths
        assert filepaths, "paths not specified!"
        self.pathRegexs = []
        for path in filepaths:
            self.pathRegexs.append(re.compile(path))
        self.tree = tree

    def start_pulse_listener(self):
        """Start listening to pulse messages.  This method will never return.
        """

        pulse = CodeConsumer(applabel='synkamatic|%s' % socket.gethostname())
        treewords = self.tree.replace('-', '.')
        pulse.configure(topic="hg.commit.#.%s" % treewords,
                        callback=self.on_pulse_message,
                        durable=False)
        try:
            pulse.listen()
        except KeyboardInterrupt:
            # gracefully exit
            sys.exit()

    def on_matching_commit(self, data):
        """This method is called whenever a pulse message is received
           that contains affected files which match |self.paths|.
        """

        print 'commit matched'
        import json
        print json.dumps(data, indent=2)

    def on_pulse_message(self, data, message):
        """This callback is invoked by the pulse library whenever it receives
           a message matching the topic it was configured with.
        """

        # Important!  Acknowledge the message so it doesn't hang around
        # forever on the pulse server.
        message.ack()

        # See if the affected files in the commit match any of our paths.
        for affectedFile in data.get('payload', {}).get('affected_files', []):
            for path in self.pathRegexs:
                if path.match(affectedFile):
                    self.on_matching_commit(data)


