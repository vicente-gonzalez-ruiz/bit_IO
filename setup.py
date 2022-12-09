#!/usr/bin/env python

from setuptools import setup

setup(name='bit_IO',
      version='1.0',
      # list folders, not files
      packages=['bit_IO'],
      scripts=['make -C bit_IO/src/bit_IO/']
      )
