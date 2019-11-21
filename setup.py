from setuptools import setup, find_packages
from mylibrary import __version__

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
# __version__ = ns.get('__version__')
# assert __version__
# del ns

setup(
    version=__version__,
)
