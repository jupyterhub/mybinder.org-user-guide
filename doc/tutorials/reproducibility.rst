Ensure reproducibility for your Binder repository
=================================================

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

When exporting a conda environment, you can add the conda-forge broken channel (``conda-forge/label/broken``) as a low-priority channel in your exported ``environment.yml`` file in order to maximize durability. Thus, if a package is marked broken after you froze the environment, said package will still install during the Binder image build process. Only do this when you intend to truly freeze the environment.

For example (in ``environment.yml``):

  .. code-block:: yaml

      channels:
        - conda-forge
        - defaults
        - conda-forge/label/broken

Using Dockerfiles
-----------------

Ensuring reproducibility with Dockerfiles comes with its own set of challenges.
For more information and best-practices when using Dockerfiles for Binder,
see :doc:`dockerfile`.
