#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '1.0.0'

requirements = ['PyYAML']

test_requirements = []

# get description from README.rst
def get_long_description():
    description = ''
    with open('README.md') as stream:
        description = stream.read()
    return description

setup(
    name='plumbery',
    version=__version__,
    description="Cloud automation at Dimension Data with Apache Libcloud",
    long_description=get_long_description(),
    author="Bernard Paques",
    author_email='bernard.paques@gmail.com',
    url='https://github.com/DimensionDataCBUSydney/plumbery',
    packages=['plumbery-contrib'],
    package_dir={'plumbery-contrib': 'fittings'},
    include_package_data=True,
    install_requires=requirements,
    license='Apache License (2.0)',
    zip_safe=False,
    keywords='plumbery-contrib',
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
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
