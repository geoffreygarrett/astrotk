.. include:: _templates/style.rst

.. image:: _static/astrotk.png
   :width: 150px
   :align: center

*********************************************
Welcome to the :cyan:`astrotk` documentation!
*********************************************

.. image:: _static/mission-phases.png
   :width: 650px
   :align: center


The :cyan:`astrotk` is an astrodynamics toolkit that is a project intended towards developing a Python interface with `TU Delft Astrodynamic Toolbox (TUDAT)`_.

Current features are:

* Conversion between Cartesian state vector, Classical orbital elements and Spherical coordinates.

Planned features are:

* Reference frame transformations according to the nomenclature and symbols in `AE3202 Flight Dynamics`_.
* Customizable genetic algorithm module for initial interplanetary trajectory optimisation estimations using patched conics.
* ITRF, GCRF & ICRF transformations.
* The unknown content of the next `AE4878 Mission Geometry & Orbit Design assignment 2`_!

.. _AE3202 Flight Dynamics: https://studiegids.tudelft.nl/a101_displayCourse.do?course_id=45367&_NotifyTextSearch_
.. _TU Delft Astrodynamic Toolbox (TUDAT): http://tudat.tudelft.nl/
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

Install :cyan:`astrotk` and its dependencies::

   pip3 install .


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. toctree::
   :maxdepth: 3
   :hidden:

   self
   preface/index
   twobody/index
   simulator/index
   bodies/index
   orbit_design/index
   orbit_determination/index
   tudastrotk/index
