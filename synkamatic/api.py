"""
generic API class for synkamatic
"""
import json
from mozillapulse.consumers import CodeConsumer
import socket
import sys


class Synkamatic(object):
    """
    sync mozilla repositories <-> github
    using pulse messages for communication and
    bugzilla and github pull-requests as
    human-moderatable media
    """

    paths = [] # a list of path prefixes to match against paths in hg
    github = None # github repository
    bugzilla = 'https://api-dev.bugzilla.mozilla.org/latest/' # REST API for bugzilla
    reviewer = None # reviewer for github -> bugzilla patches
    cc = [] # bugzilla users to CC for github -> bugzilla patches

    def __init__(self, github=None, paths=None, tree='mozilla-central',
                 pulsefile=None):
        self.github = github or self.github
        assert self.github, "github repository not specified!"
        self.path = paths or self.paths
        assert self.paths, "paths not specified!"
        self.tree = tree
        self.pulsefile = pulsefile

    def start_pulse_listener(self):
        """Start listening to pulse messages.  This method will never return.
        """

        treewords = self.tree.replace('-', '.')
        pulse = CodeConsumer(applabel='synkamatic|%s' % socket.gethostname(),
                             heartbeat=True)
        pulse.configure(topic="hg.commit.#.%s" % treewords,
                        callback=self.on_pulse_message,
                        durable=False)

        if self.pulsefile:
            self.on_pulse_message(json.loads(open(self.pulsefile, 'r').read()), None)

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
        print json.dumps(data, indent=2)

    def on_pulse_message(self, data, message):
        """This callback is invoked by the pulse library whenever it receives
           a message matching the topic it was configured with.
        """

        # Important!  Acknowledge the message so it doesn't hang around
        # forever on the pulse server.
        if message:
            message.ack()

        # See if the affected files in the commit match any of our paths.
        for affectedFile in data.get('payload', {}).get('affected_files', []):
            for path in self.paths:
                if affectedFile.startswith(path):
                    self.on_matching_commit(data)


