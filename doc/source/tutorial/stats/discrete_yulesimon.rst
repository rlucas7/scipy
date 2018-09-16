
.. _discrete-yulesimon:

Yule-Simon Distribution
====================

The Yule-Simon random variable counts the number of 

A Yule-Simon random variable has been used to model the counts of biological taxa, species within a genus etc. and has also been used to model the rank distribution of cities and to model the evolution of citation networks and more generally the vertex degree distribution of other network processes. 
The support of the distribution is the non-negative integers :math: `\{1,2,3,\dots \}` and the single parameter :math: `\alpha >0`. 
AIf the parameter :math: `0<\alpha<1` the mean is infinite, similar statements apply to the second and higher non-central moments. 
The probability mass function (pmf) for the Yule-Simon distribution is: 

.. math::
   :nowrap:
    \begin{eqnarray*} p\left(k;\alpha\right) & = & \alpha B(k, \alpha+1) \end{eqnarray*}
.. math::

where :math: `B(a,b)` is the beta function 

Implementation: `scipy.stats.yulesimon`
