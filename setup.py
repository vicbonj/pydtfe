import os
from setuptools import find_packages, setup

import pydtfe

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name = 'pydtfe',
    version=pydtfe.__version__,
    author = "Victor Bonjean",
    author_email = "victor.bonjean@obspm.fr",
    description = "Create DTFE density map in 2 and 3 dimensions",
    packages=find_packages(),
    include_package_data=True,
    url = "https://github.com/vicbonj/density",
    long_description=open('README.md').read(),
)
