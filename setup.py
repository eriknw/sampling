#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import sampling

setup(
    name='sampling',
    version=sampling.__version__,
    description='Randomly sample iterables',
    url='http://github.com/eriknw/sampling/',
    author='https://raw.github.com/eriknw/sampling/master/AUTHORS.md',
    maintainer='Erik Welch',
    maintainer_email='erik.n.welch@gmail.com',
    license='BSD',
    keywords='sampling sample statistics random iterators',
    packages=[
        'sampling',
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering',
    ],
    long_description=open('README.md').read() if exists("README.md") else "",
    zip_safe=False,
)
