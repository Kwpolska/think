#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup


setup(name='think',
      version='0.1.2',
      description='Terminal Think Music',
      keywords='think music, Jeopardy!, game show',
      author='Chris Warrick',
      author_email='chris@chriswarrick.com',
      url='https://github.com/Kwpolska/think',
      license='3-clause BSD',
      long_description=io.open('./README.rst', 'r', encoding='utf-8').read(),
      platforms='POSIX',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: System Administrators',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: POSIX',
                   'Topic :: Multimedia :: Sound/Audio :: Players',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4'],
      py_modules=['think'],
      entry_points={
          'console_scripts': [
              'think = think:main',
          ]
      },
      )
