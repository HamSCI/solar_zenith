#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='solar_zenith',
      version='0.1',
      description='Solar Zenith Angle and Geopack',
      author='Nathaniel A. Frissell',
      author_email='nathaniel.frissell@scranton.edu',
      url='https://hamsci.org',
      packages=['solar_zenith'],
      install_requires=requirements
     )
