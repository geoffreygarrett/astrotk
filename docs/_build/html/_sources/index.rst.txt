.. astrotk documentation master file, created by
   sphinx-quickstart on Thu Nov 22 00:53:20 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

*************************************
Welcome to the astrotk documentation!
*************************************

.. image:: https://travis-ci.org/rtfd/sphinx_rtd_theme.svg?branch=master
   :target: https://travis-ci.org/rtfd/sphinx_rtd_theme
   :alt: Build Status
.. image:: https://img.shields.io/pypi/l/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme/
   :alt: License
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. image:: _static/mission_phases.png
   :width: 675px
   :align: center

The ``astrotk`` is a Astrodynamics toolkit that is a project intended towards developing a Python interface with `TU Delft Astrodynamic Toolbox`_.

Current features are:

* Conversion between Cartesian state vector, Classical orbital elements and Spherical coordinates.

Planned features are:

* Reference frame transformations according to the nomenclature and symbols in `AE3202 Flight Dynamics`_.
* Customizable genetic algorithm module for initial interplanetary trajectory optimisation estimations using patched conics.
* ITRF, GCRF & ICRF transformations.
* The unknown content of the next `AE4878 Mission Geometry & Orbit Design assignment 2`_!

.. _AE3202 Flight Dynamics: https://studiegids.tudelft.nl/a101_displayCourse.do?course_id=45367&_NotifyTextSearch_
.. _TU Delft Astrodynamic Toolbox: http://tudat.tudelft.nl/
.. _AE4878 Mission Geometry & Orbit Design assignment 2: https://www.merriam-webster.com/dictionary/awesome

.. seealso::

   Choice of object oriented design and implementation of astrodynamics in
   Python is acknowledged to be adapted from `Poliastro`_, which I used extensively during the
   Design Synthesis Exercise (DSE).

.. _Poliastro: https://docs.poliastro.space/en/latest/

Installing
==========

Clone the repository from GitHub::

   git clone https://github.com/ggarrett13/astrotk.git

Navigate to the repository folder::

   cd /astrotk

Install ``astrotk`` and its dependencies::

   pip3 install .


Changelog
=========
.. toctree::
   :maxdepth: 2

   changelog

Modules
=======

.. toctree::
   :maxdepth: 2
   :caption: Modules

   twobody/state
   twobody/utils

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Verification:

   example/twobody/iss
   example/twobody/cryosat2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
