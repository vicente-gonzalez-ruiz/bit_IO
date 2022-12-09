#!/usr/bin/env python

from setuptools import setup

setup(name='bit_IO',
      version='1.0',
      # list folders, not files
      packages=['src/bit_IO'],
      scripts=['scripts/compile']
      )
