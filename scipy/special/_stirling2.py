import numpy as np
import scipy.special as sc

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
    """Compute Stirling numbers of second kind with arbitrary precision ints

     Computes from the bottom up using the recurrence relation
     stirling2(n, k) = k * stirling2(n, k - 1) + stirling2(n - 1, k - 1)
     with boundary conditions: stirling2(n, 1) = 1, stirling2(n, n) = 1.
     The below implementation only computes the Stirling numbers necessary
     for the final result. Arranging the Stirling numbers in a triangle
     with stirling2(1, 1) at the top, n increasing from top to bottom and
     k increasing from left to right, to compute stirling2(n, k) one
     only needs to compute the values in the parallelogram with vertices at
     (1, 1), (k, k), (k, 1), (n, k). This is illustrated in the ASCII diagram
     below for stirling2(5, 3).

     x
     x x
     x x x
     o x x o
     o o x o o
     o o o o o o

     To minimize the memory needed, if k <= n - k + 1, an array of length k
     is allocated and the cells of the parallelogram are filled in order from
     left to right and then top to bottom. If k > n - k + 1, an array of
     length n - k + 1 is allocated and the cells are filled in order from top
     to bottom and then left to right. See
     https://github.com/scipy/scipy/pull/18103#discussion_r1130036365
    """
    # Check for boundary cases.
    if n == 0 and k == 0:
        return 1
    if k <= 0 or k > n or n < 0:
        return 0

    # DLMF 26.8.15 https://dlmf.nist.gov/26.8#E15
    if k == n - 1:
        return sc.comb(n, 2, exact=True)

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
