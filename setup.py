from importlib import import_module
import os

from setuptools import setup, find_packages


_mod = import_module('ex4mple')
_root = os.path.dirname(os.path.abspath(__file__))
setup(
    name='ex4mple',
    version=_mod.__version__,
    author='Tomohiro NAKAMURA',
    author_email='quickness.net@gmail.com',
    url='https://github.com/jptomo/test-with-jenkins-and-circle-ci.py',
    description='Example for Jenkins and CircleCI Integration',
    long_description=open(os.path.join(_root, 'README.md')).read(),
    packages=find_packages('ex4mple'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT License',
    extras_require={
        'test': ['pytest', 'pytest-cov'],
        'packaging': ['wheel'],
    }
)
