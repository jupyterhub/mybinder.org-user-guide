====================
Binder Documentation
====================

.. image:: https://badges.gitter.im/jupyterhub/binder.svg
   :alt: Join the chat at https://gitter.im/jupyterhub/binder
   :target: https://gitter.im/jupyterhub/binder?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

**Binder** allows you to create custom computing environments that can be shared
and used by many remote users. It is powered by `BinderHub <https://github.com/jupyterhub/binderhub>`_,
which is an open-source tool that deploys the Binder service in the cloud.
One-such deployment lives here, at `mybinder.org <https://mybinder.org>`_, and is free to use.
For more information about the mybinder.org deployment and the team that runs it, see
:ref:`about`.

This documentation provides information for those who
wish to use a pre-existing BinderHub deployment such as `mybinder.org <https://mybinder.org>`_.
If you'd like documentation on how to create and administer your own BinderHub deployment,
see the `BinderHub documentation <http://binderhub.readthedocs.io>`_, which
guides you through deploying your own BinderHub.

See the `Binder Examples <https://github.com/binder-examples>`_ GitHub
organization for sample Binder repositories demonstrating its functionality.

.. note::

   Binder is a research pilot, whose main goal is to understand usage patterns
   and workloads for future evolution and development. It is not a service that
   can be relied on for critical operations.

Using Binder
============

The following sections cover the basics of how to use a Binder service.

.. toctree::
   :caption: Getting started with Binder
   :maxdepth: 2

   introduction
   using

.. toctree::
   :caption: How to...
   :maxdepth: 1

   howto/languages
   howto/user_interface
   howto/badges

.. toctree::
   :maxdepth: 2
   :caption: Tutorials and in-depth guides

   tutorials/reproducibility
   tutorials/dockerfile


Sample repositories and configuration
=====================================

The following is a list of sample repositories showing off various things
you can do with Binder.

.. toctree::
   :maxdepth: 1
   :caption: Sample repositories and configuration

   examples
   sample_repos
   config_files


Advanced usage
==============

These pages cover more advanced topics in the Binder ecosystem, as well
as resources for more information.

.. toctree::
   :maxdepth: 1

   user-guidelines
   faq
   status
   about
   reliability
   more-info

.. _citing:

Citing Binder
=============

If you publish work that uses Binder, please consider citing the
`Binder paper from the 2018 SciPy proceedings <http://conference.scipy.org/proceedings/scipy2018/project_jupyter.html>`_!

Here is a citation that you can use:

.. code-block:: none

   Jupyter et al., "Binder 2.0 - Reproducible, Interactive, Sharable
   Environments for Science at Scale." Proceedings of the 17th Python
   in Science Conference. 2018. 10.25080/Majora-4af1f417-011