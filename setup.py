import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pydtfe",
    version = "1.0",
    author = "Victor Bonjean",
    author_email = "victor.bonjean@obspm.fr",
    description = ("Create DTFE density map in 2 and 3 dimensions"),
    keywords = "example documentation tutorial",
    url = "https://github.com/vicbonj/density",
    packages=['density'],
    long_description=read('README.md'),
)
