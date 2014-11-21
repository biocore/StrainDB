#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Copyright (c) 2013, The StrainDB Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

__version__ = "0.1.0-dev"

from setuptools import setup
from glob import glob


classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering :: Bio-Informatics
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Software Development :: Libraries :: Python Modules
    Programming Language :: Python
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: OS Independent
    Operating System :: POSIX :: Linux
    Operating System :: MacOS :: MacOS X
"""

long_description = """StrainDB is a database for strain genomes"""

classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='sdb',
      version=__version__,
      long_description=long_description,
      license="BSD",
      description='StrainDB',
      author="StrainDB development team",
      author_email="josenavasmolina@gmail.com",
      url='http://github.com/biocore/StrainDB',
      test_suite='nose.collector',
      packages=['sdb'],
      extras_require={'test': ["nose >= 0.10.1", "pep8", 'mock'],
                      'doc': ["Sphinx >= 1.2.2", "sphinx-bootstrap-theme"]},
      install_requires=[],
      classifiers=classifiers
      )
