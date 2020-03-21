import re
import sys
import os
from codecs import open
from setuptools import setup

# Django 2.2 requires at least Python 3.5
PY32     = sys.version_info == (3, 2) 
LT_PY35  = sys.version_info < (3, 5)
GTE_PY35 = sys.version_info >= (3, 5)
GTE_PY36 = sys.version_info >= (3, 6)

tests_require = ['nose', 'mock', 'testfixtures', 'blinker', 'Flask>=1.0']

if sys.version_info[0:2] <= (3, 5):
    tests_require.append('Django>=1.11,<=2.2')
else:
    tests_require.append('Django>3.0,<4.0')

# Ugly fix for testfixtures on Python 3.2
if PY32:
    tests_require.remove('testfixtures')
    tests_require.append('testfixtures==5.3.1')


def get_version():
    with open('honeybadger/version.py', encoding='utf-8') as f:
        return re.search(r'^__version__ = [\'"]([^\'"]+)[\'"]', f.read(), re.M).group(1)


setup(
    name='honeybadger',
    version=get_version(),
    description='Send Python and Django errors to Honeybadger',
    url='https://github.com/honeybadger-io/honeybadger-python',
    author='Dave Sullivan',
    author_email='dave@davesullivan.ca',
    license='MIT',
    packages=['honeybadger', 'honeybadger.contrib'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Monitoring'
    ],
    install_requires=[
        'psutil',
        'six'
    ],
    test_suite='nose.collector',
    tests_require=tests_require
)
