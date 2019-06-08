import unittest

import numpy as np

import somecode.logic


def test_code() -> None:
    pi = somecode.logic.get_pi()
    assert np.abs(pi - 3.14159) < 1e-5