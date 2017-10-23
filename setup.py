#!/usr/bin/env python

from distutils.core import setup

desc = """\
CPLEX SOLVE
==============

This package provide two simplified way to use the CPLEX python API.

1. from_matrices, where you can provide the matrices corresponding to the simplex tableau of a given problem
2. from_template, where you can privides variables and constraints in a more convenient way following a special template. (see the documentation)
"""

setup(
    # Application name:
    name='cplex_solve',
    # Version number (initial):
    version='0.1.1',
    description='Simplified way to use the CPLEX Python API',
    # Application author details:
    author='Alexandre Couedelo',
    author_email='nokwebspace@gmail.com',
    # Details
    url='https://github.com/xNok/OR_CPLEX_solve',
    # Packages
    packages=['cplex_solve']
    # Dependent packages (distributions)
)

