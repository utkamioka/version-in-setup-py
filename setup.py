#!/usr/bin/python

from setuptools import setup, find_packages
# from mylibrary import __version__

# # ready for Python2 and 3
# # > $ py -2 setup.py --version
# # > $ py -3 setup.py --version
# packages = find_packages(exclude=['tests'])
#
# ns = dict()
# for package in packages:
#     import os
#     version_file = os.path.join(package, '__version__.py')
#     if os.path.exists(version_file):
#         with open(version_file, mode='rt') as f:
#             eval(compile(f.read(), version_file, 'exec'), dict(), ns)
#             break
#
# __version__ = ns['__version__']
# del ns

setup(
    # version=__version__,
)
