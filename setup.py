#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup

import pydtfe


setup(
    name='pydtfe',
    version="2.0.0",
    author="Victor Bonjean",
    author_email="victor.bonjean40@gmail.com",
    description="Create DTFE density map in 2 and 3 dimensions",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/vicbonj/pydtfe",
    download_url="https://github.com/vicbonj/pydtfe/archive/0.1.tar.gz",
    long_description=open('README.md').read(),
)
