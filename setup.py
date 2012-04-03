"""
setup packaging script for synkamatic
"""

import os

version = "0.0"
dependencies = ['mozillapulse']

# allow use of setuptools/distribute or distutils
kw = {}
try:
    from setuptools import setup
    kw['entry_points'] = """
      [console_scripts]
      synkamatic = synkamatic.main:main
      synk-mozbase = synkamatic.mozbase:main
"""
    kw['install_requires'] = dependencies
except ImportError:
    from distutils.core import setup
    kw['requires'] = dependencies

try:
    here = os.path.dirname(os.path.abspath(__file__))
    description = file(os.path.join(here, 'README')).read()
except IOError:
    description = ''


setup(name='synkamatic',
      version=version,
      description="Synkamatic helps to automate the syncing of changes between mirrored Mozilla hg and github repos",
      long_description=description,
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      author='Jonathan Griffin',
      author_email='jgriffin@mozilla.com',
      url='https://github.com/jonallengriffin/synkamatic',
      license='MPL',
      packages=['synkamatic'],
      include_package_data=True,
      zip_safe=False,
      **kw
      )
