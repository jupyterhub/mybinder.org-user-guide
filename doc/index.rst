Binder Documentation
====================

.. image:: https://badges.gitter.im/jupyterhub/binder.svg
   :alt: Join the chat at https://gitter.im/jupyterhub/binder
   :target: https://gitter.im/jupyterhub/binder?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

**Binder** allows you to create custom computing environments that can be shared
and used by many remote users. It is powered by `BinderHub <https://github.com/jupyterhub/binderhub>`_,
which is an open-source tool that deploys the Binder service in the cloud.
One-such deployment lives here, at `mybinder.org <https://mybinder.org>`_, and is free to use.

This documentation provides information for those who
wish to use a pre-existing Binder deployment such as `mybinder.org <https://mybinder.org>`_.
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
------------

The following sections cover the basics of how to use a Binder service.

.. toctree::
   :maxdepth: 2

   introduction
   using
   user-guidelines

Sample repositories
-------------------

The following is a list of sample repositories showing off various things
you can do with Binder.

.. toctree::
   :maxdepth: 2

   sample_repos

Advanced
--------

These sections cover more advanced topics in the Binder ecosystem, as well
as resources for more information.

.. toctree::
   :maxdepth: 2

   dockerfile
   reproducibility
   faq
   reliability
   more-info

Binder in the wild
------------------

This is a list of private or public `Binder <http://binderhub.readthedocs.io>`_
instances. If you would like to list yours here `open an issue <https://github.com/jupyterhub/binder/issues/new>`
and let us know.

A list like this helps the project prioritize work based on actual usage patterns
and gives us (and our funders) concrete evidence of adoption.

* Be the first one! `Open an issue <https://github.com/jupyterhub/binder/issues/new>`.
