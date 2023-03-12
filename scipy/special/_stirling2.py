import numpy as np
from scipy.special._ufuncs import _stirling2_approx


def stirling2(n, k, exact=True):
    """Needs updated docstring."""
    if exact:
        return _stirling2_pyint(n, k)
    else:
        return _stirling2_approx(n, k)


def _stirling2_pyint(n, k):
    if n == 0 and k == 0:
        return 1
    if k <= 0 or k > n or n < 0:
        return 0
    if k <= n - k + 1:
        current = [1]*k
        for i in range(1, n - k + 1):
            for j in range(1, k):
                current[j] = (j+1) * current[j] + current[j-1]
    else:
        current = [1]*(n - k + 1)
        for i in range(1, k):
            for j in range(1, n - k + 1):
                current[j] = (i+1) * current[j-1] + current[j]
    return current[-1]
