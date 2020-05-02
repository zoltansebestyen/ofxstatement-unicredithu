#!/usr/bin/env python3
"""Setup
"""
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from distutils.core import setup
import unittest
import sys

class RunTests(TestCommand):
    """New setup.py command to run all tests for the package.
    """
    description = "run all tests for the package"

    def finalize_options(self):
        super(RunTests, self).finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        tests = unittest.TestLoader().discover('src/ofxstatement')
        runner = unittest.TextTestRunner(verbosity=2)
        res = runner.run(tests)
        sys.exit(not res.wasSuccessful())

version = "0.0.2"

with open('README.rst') as f:
    long_description = f.read()

setup(name='ofxstatement-unicredithu',
      version=version,
      author="Zoltan Sebestyen",
      author_email="zoltan.sebestyen@gmail.com",
      url="https://github.com/zoltansx/ofxstatement-unicredithu",
      description=("ofxstatement plugin for the Hungarian bank Unicredit"),
      long_description=long_description,
      license="GPLv3",
      keywords=["ofx", "banking", "statement"],
      cmdclass={'test': RunTests},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU Affero General Public License v3'],
      packages=find_packages('src'),
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement':
          ['unicredithu = ofxstatement.plugins.unicredit:UnicreditPlugin']
          },
      package_dir={'': 'src'},
      install_requires=['ofxstatement',
                        'setuptools'
                        ],
      extras_require={'test': ["mock"]},
      tests_require=["mock"],
      include_package_data=True,
      zip_safe=True
      )
