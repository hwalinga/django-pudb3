#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os

from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='django-pudb3',
    version='0.2.0',
    description='Django middleware to view exceptions in PuDB.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/hielkewalinga/django-pudb3/',
    license='MIT',
    author='Hielke Walinga',
    author_email='hielkewaligna@gmail.com',
    py_modules=['django_pudb'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
