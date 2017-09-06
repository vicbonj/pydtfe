#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup

import pydtfe


setup(
    name='pydtfe',
    version=pydtfe.__version__,
    author="Victor Bonjean",
    author_email="victor.bonjean@obspm.fr",
    description="Create DTFE density map in 2 and 3 dimensions",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/vicbonj/pydtfe",
    long_description=open('README.md').read(),
)
