import numpy as np
from scipy.special._ufuncs import _stirling2_approx


def stirling2(n, k, exact=True):
    """stirling2(n, k)

    Stirling number of the second kind. Counts the number of non-empty subsets
    of `n` set items that can be made with `k` non-empty subsets. Both `n` and
    `k` should be non-negative integers, Negative integers for either `n` or
    `k` cause the function to return `0`.

    Parameters
    ----------
    n : int, array_like
        The number of items in the set
    k : int, array_like
        The number of non-empty subsets to be made out of the n elements

    Returns
    -------
    int, scalar or ndarray
        The number of ways to make k non-empty subsets out of n elements

    Notes
    -----
    - Array arguments accepted only for exact=False case.

    Examples
    --------
    >>> import scipy.special as sc
    >>> sc.stirling2(0,0)
    1
    >>> sc.stirling2(3,0)
    0
    >>> sc.stirling2(4,2)
    7
    >>> sc.stirling2(4,3)
    6
    >>> sc.stirling2(26,10)
    13199555372846848005

    See Also
    --------
    comb, factorial
    """
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
