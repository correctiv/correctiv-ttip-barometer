#!/usr/bin/env python

import codecs
import re
import os

from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="correctiv_ttip_barometer",
    version='0.0.1',
    url='https://github.com/correctiv/correctiv-ttip-barometer',
    license='MIT',
    description="correctiv ttip barometer",
    long_description=read('README.md'),
    author='Simon Jockers',
    author_email='simon.jockers@correctiv.org',
    packages=find_packages(),
    install_requires=[
        'Django',
        'django-pagedown',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
