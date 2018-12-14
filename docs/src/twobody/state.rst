
*********************
State Transformations
*********************

The planets of the solar system are defined in this module.

For example, earth can be imported as follows:

.. code:: python

  from orbital.bodies import earth

The example definition of a ``ClassicalState()`` object undergoing transformation to
a ``VectorState()`` follows:

.. code:: python

   >>> from astrotk import twobody
   >>> import astropy.units as u
   >>> from astrotk.AE4878.bodies import Earth

   >>> classical_args = [
    7096137.00 * u.m,
    0.0011219 * u.dimensionless_unscaled,
    92.0316 * u.deg,
    296.1384 * u.deg,
    120.6878 * u.deg,
    239.5437 * u.deg,
    239.5991 * u.deg,
    239.6546 * u.deg
   ]
   >>> classical_state = twobody.ClassicalState(attractor=Earth(), *classical_args)

   >>> classical_state.prettyprint()

   >>> vector_state = classical_state.to_vectors().prettyprint()

