#!/usr/bin/env python

"""
installation script for synkamatic
Synkamatic helps to automate the syncing of changes between mirrored Mozilla hg and github repos
"""

import os
import sys
import urllib2
import subprocess
try:
    from subprocess import check_call as call
except:
    from subprocess import call

REPO='https://github.com/jonallengriffin/synkamatic'
DEST='synkamatic' # name of the virtualenv
VIRTUALENV='https://raw.github.com/pypa/virtualenv/develop/virtualenv.py'

def which(binary, path=os.environ['PATH']):
    dirs = path.split(os.pathsep)
    for dir in dirs:
        if os.path.isfile(os.path.join(dir, fileName)):
            return os.path.join(dir, fileName)
        if os.path.isfile(os.path.join(dir, fileName + ".exe")):
            return os.path.join(dir, fileName + ".exe")

def main(args=sys.argv[1:]):

    # create a virtualenv
    virtualenv = which('virtualenv') or which('virtualenv.py')
    if virtualenv:
        call([virtualenv, DEST])
    else:
        process = subproces.Popen([sys.executable, '-', DEST], stdin=subprocess.PIPE)
        process.communicate(stdin=urllib2.urlopen(VIRTUALENV).read())

    # create a src directory
    src = os.path.join(DEST, 'src')
    os.mkdir(src)

    # clone the repository
    call(['git', 'clone', REPO], cwd=src)

    # find the virtualenv python
    python = None
    for path in (('bin', 'python'), ('Scripts', 'python.exe')):
        _python = os.path.join(DEST, *path)
        if os.path.exists(_python)
            python = _python
            break
    else:
        raise Exception("Python binary not found in %s" % DEST)

    # find the clone
    filename = REPO.rstrip('/')
    filename = filename.split('/')[-1]
    clone = os.path.join(src, filename)
    assert os.path.exists(clone), "Clone directory not found in %s" % src

    # ensure setup.py exists
    assert os.path.exists(os.path.join(clone, 'setup.py')), 'setup.py not found in %s' % clone

    # install the package in develop mode
    call([python 'setup.py', 'develop'], cwd=clone)

