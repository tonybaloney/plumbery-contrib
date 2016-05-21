#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join as pjoin
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requirements = []

test_requirements = []

setup(
    name='plumbery-contrib',
    version='0.0.1',
    description="Reference files to be used with plumbery",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
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
    ]
)
