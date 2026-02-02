# Security

In general the core maintainers of SciPy are scientific experts in their domains and not security experts.
We are security conscious and have mechanisms for resolving identified security issues.

We follow the guidelines under the [NumPy security guidelines](https://numpy.org/devdocs/reference/security.html)
in addition to this document. 

# Data
For working with untrusted data [these guidelines](https://numpy.org/devdocs/reference/security.html#important) generally apply.
An exception is the [datasets directory](https://github.com/scipy/scipy/tree/main/scipy/datasets) where 
we rely on the [pooch](https://github.com/fatiando/pooch) dependency to fetch data and use
[sha256 codes](https://github.com/scipy/scipy/blob/main/scipy/datasets/_registry.py) to verify the downloads.

# Releases
To mitigate the risk of supply chain attacks we rely on the [SciPy](https://github.com/scipy/scipy-release) release repo
which is modeled after the [Numpy release](https://github.com/numpy/numpy-release) process.

General security guidelines on the scipy-release repo:
- We require a linear history, so commit history is easy to inspect
- We require branch protection etc. and apply best practices
- We perform only wheels.yml runs, and optionally a security-related linter action
- We required all release artifacts to be built inside this repository on GitHub Actions runners
- We do not allow self-hosted runners on this repository
- We allow cross-compiling provided we are able to afford the billing and have adequate maintainer time
- We perform verification of the test suite passing after cross compilation either on the [scipy repo](https://github.com/scipy/scipy/tree/main/)
  or under QEMU

We use pypi [trusted publishing](https://docs.pypi.org/trusted-publishers/).

# Disclosure
To report vulnerabilities please review the guidelines here to determine whether the vulnerability indeed needs to be reported
on the SciPy repo and not an upstream dependency. If the detected vulnerability requires remediation in an upstream dependency
we ask that you report the disclosure to the upstream dependency.

## Vendored Dependencies
Exceptions to the upstream dependency policy would be if a vulnerability was in a vendored dependency.
Vendored dependencies are included in [sub_projects](https://github.com/scipy/scipy/tree/main/subprojects).
Vendored dependencies are not currently included with the sites [SBOM](https://github.com/scipy/scipy/dependency-graph/sbom)
file exports.
