========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/behave-generator/badge/?style=flat
    :target: https://readthedocs.org/projects/behave-generator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/accraze/behave-generator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/accraze/behave-generator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/accraze/behave-generator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/accraze/behave-generator

.. |requires| image:: https://requires.io/github/accraze/behave-generator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/accraze/behave-generator/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/accraze/behave-generator/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/accraze/behave-generator

.. |codecov| image:: https://codecov.io/github/accraze/behave-generator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/accraze/behave-generator

.. |version| image:: https://img.shields.io/pypi/v/behave-generator.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/behave-generator

.. |downloads| image:: https://img.shields.io/pypi/dm/behave-generator.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/behave-generator

.. |wheel| image:: https://img.shields.io/pypi/wheel/behave-generator.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/behave-generator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/behave-generator.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/behave-generator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/behave-generator.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/behave-generator


.. end-badges

Bootstrap your project to use behave bdd

* Free software: BSD license

Installation
============

::

    pip install behave-generator

Documentation
=============

https://behave-generator.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
