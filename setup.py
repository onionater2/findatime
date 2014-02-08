# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import findatime
version = findatime.__version__

setup(
    name='findatime',
    version=version,
    author='',
    author_email='amy.skerry@gmail.com',
    packages=[
        'findatime',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['findatime/manage.py'],
)