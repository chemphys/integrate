"""
This file contains the implementation of the Simpson rule
"""

import numpy as np


def evaluate(bounds, func):
    """

    Evaluates simpsons rules on an array of values and a function pointer.

.. math::

    \int _{a}^{b} = \sum _i ...

    Parameters
    ----------
    bounds : array_like
        An array of dimention two with the starting and ending points.
    func : function
        Produces the integrand at a point

    Returns
    -------
    integral : float
    The integral function between the bounds

    """

    if len(bounds) != 2:
        raise ValueError("Bounds should be of length 2. Found %d." % len(bounds))
    a = bounds[0]
    b = bounds[1]
    ya = func(a)
    yb = func((a + b) / 2.0)
    yc = func(b)
    I = (b - a) * (ya + 4.0 * yb + yc) / 6.0
    return I
