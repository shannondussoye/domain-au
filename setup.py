#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Package meta-data.
NAME = 'Domain Australia Scraper'
DESCRIPTION = 'A personal project that scrapes domain.com.au for analysis using additional features e.g. fare'
URL = 'https://github.com/shannondussoye/domain-au'
EMAIL = 'me@example.com'
AUTHOR = 'Shannon Dussoye'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

# What packages are required for this module to be executed?
# REQUIRED = [
#     'requests', 'pandas', 'bs4','json'
# ]

from setuptools import setup, find_packages

setup(name=NAME,
      version='0.0.1',
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=EMAIL,
      url=URL,
      packages=find_packages(),
     )