1# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

name = 'psyquizz.quizz1'
version = '0.1'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()


install_requires = [
    'nva.psyquizz',
    ]

tests_require = [
    'zope.testbrowser >= 5.2',
    'z3c.etestbrowser',
    ]

setup(name=name,
      version=version,
      description=(""),
      long_description=readme + '\n\n' + history,
      keywords='',
      author='',
      author_email='',
      url='',
      license='Proprietary',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['psyquizz'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
