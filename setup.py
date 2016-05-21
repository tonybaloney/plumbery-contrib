#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join as pjoin
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requirements = ['plumbery']

test_requirements = []

# get description from README.rst
def get_long_description():
    description = ''
    with open('README.rst') as stream:
        description = stream.read()
    return description

setup(
    name='plumbery-contrib',
    version='0.0.1',
    description="Reference files to be used with plumbery",
    long_description=get_long_description(),
    author="Bernard Paques",
    author_email='bernard.paques@gmail.com',
    url='https://github.com/DimensionDataCBUSydney/plumbery-contrib',
    packages=[],
    package_dir={},
    include_package_data=True,
    install_requires=requirements,
    license='Apache License (2.0)',
    zip_safe=False,
    keywords='plumbery',
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Customer Service',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
