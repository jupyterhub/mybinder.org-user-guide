.. _binder-docs:

====================
Binder Documentation
====================

.. image:: https://badges.gitter.im/jupyterhub/binder.svg
   :alt: Join the chat at https://gitter.im/jupyterhub/binder
   :target: https://gitter.im/jupyterhub/binder

.. image:: https://img.shields.io/discourse/https/discourse.jupyter.org/users.svg?colorB=blue&label=discourse&style=flat
   :alt: Join our community Discourse page at https://discourse.jupyter.org
   :target: https://discourse.jupyter.org


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

.. toctree::
   :maxdepth: 2

   index-getting-started


How-To guides and Tutorials
===========================

The following sections discuss some more in-depth topics on preparing and sharing
your Binder repository. How-To guides are shorter, actionable patterns that
accomplish something specific. Tutorials are more high-level and thorough,
and often cover more conceptual topics.

.. toctree::
   :maxdepth: 2

   howto/index
   tutorials/index

`The Turing Way <https://github.com/alan-turing-institute/the-turing-way>`_ also maintains a Zero-to-Binder tutorial in 3 common programming languages.

* `Julia <http://bit.ly/zero-to-binder-julia>`_
* `Python <http://bit.ly/zero-to-binder-python>`_
* `R <http://bit.ly/zero-to-binder-r>`_

Sample repositories and configuration
=====================================

The following is a list of sample repositories showing off various things
you can do with Binder configuration files.

.. toctree::
   :maxdepth: 2

   index-repo-reference

See the `Binder Examples <https://github.com/binder-examples>`_ GitHub
organization for more Binder repositories demonstrating its functionality.


The Binder Community
====================

These pages cover more advanced topics in the Binder ecosystem, community
guidelines for users and developers, and information about the ``mybinder.org``
service.

.. toctree::
   :maxdepth: 2
   :caption: Binder community

   index-community

.. _citing:

Citing Binder
=============

If you publish work that uses Binder, please consider citing the
`Binder paper from the 2018 SciPy proceedings <http://conference.scipy.org/proceedings/scipy2018/project_jupyter.html>`_!

Here is a citation that you can use:

.. code-block:: none

   Jupyter et al., "Binder 2.0 - Reproducible, Interactive, Sharable
   Environments for Science at Scale." Proceedings of the 17th Python
   in Science Conference. 2018. doi://10.25080/Majora-4af1f417-011

`<https://doi.org/10.25080/Majora-4af1f417-011>`_
