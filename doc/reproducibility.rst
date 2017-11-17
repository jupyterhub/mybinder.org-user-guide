Tips for reproducibility
========================

Binder will create a new Docker image the first time is run with a repository.
From then on, a new image will only be created if the commit hash changes
(if you're linking Binder to a branch and not a specific commit hash). Here
are some tips to ensure reproducibility of your Binder links even if you must
re-build your repository image:

Pin dependencies
----------------

When you install a dependency, include its version number (depending on the
language you use, the exact syntax may vary). E.g., don't just specify ``numpy``,
specify ``numpy==1.12.0``.

``pip freeze`` is a handy tool to export the exact version of every Python
package in your environment in a format that can be used in ``requirements.txt``.

``conda env export -n <env-name>`` is the equivalent for anaconda's environment.yml
file.

Using Dockerfiles
-----------------

Ensuring reproducibility with Dockerfiles comes with its own set of challenges.
For more information and best-practices when using Dockerfiles for Binder,
see :doc:`dockerfile`.
