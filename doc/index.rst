Binder Documentation
====================

.. image:: https://badges.gitter.im/jupyterhub/binder.svg
   :alt: Join the chat at https://gitter.im/jupyterhub/binder
   :target: https://gitter.im/jupyterhub/binder?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

**Binder** allows you to create custom computing environments that can be shared
and used by many remote users. This page provides information for those who
wish to use a pre-existing Binder deployment (e.g., ``mybinder.org``).

If you'd like to create and administer your own Binder deployment, see the
`BinderHub documentation <http://binderhub.readthedocs.io>`_. The BinderHub
documentation guides you through creating a cluster, deploying BinderHub, and
administering a BinderHub deployment.

.. toctree::

   dockerfile.rst

What can I do with Binder?
--------------------------

Binder makes it simple to generate reproducible computing environments from a
GitHub repository. Binder uses the BinderHub technology to generate a Docker
image from this repository. The image will have all the components that you
specify along with the Jupyter Notebooks inside. You will be able to share a URL
with users that can immediately begin interacting with this environment via the
cloud.

See the `Binder Examples <https://github.com/binder-examples>`_ GitHub
organization page for inspiration.

How much memory am I given when using Binder?
---------------------------------------------

If you or another Binder user clicks on a Binder link, the ``mybinder.org``
deployment will run the linked repository. While running, you are guaranteed
to have at least 1G of RAM. There is an upper-limit of 4GB (if you use more than
4GB your kernel will be restarted).

.. _preparing_repositories:

How do I prepare a repository for Binder?
-----------------------------------------

You can do this by making sure your repo contains:

* A collection of Jupyter Notebooks. These notebooks will be made available to
  users of your Binder.
* One (or many) text files that specify the requirements of your code. For
  example, a ``requirements.txt`` or ``environment.yml`` file. See the
  `repo2docker <https://repo2docker.readthedocs.org>`_ documentation for a list of all
  the files and environments that are supported.

All you need to do is include the files specified above in a GitHub repository.
Once that's done, navigate to ``beta.mybinder.org`` and insert the URL for
your git repository. Press ``Launch`` to automatically create your Binder.
The Binder service will be automatically send you to a live Jupyter session
connected to this repository.

.. note::

   If a previous version of the repository has already been built, Binder will
   only build a new one if the git hashes don't match. If Binder *doesn't* have
   to build a new repository, the process of connecting to the live
   computational environment is much faster.

How do I generate a Binder link to share?
-----------------------------------------

You may share a link that generates a Binder. The link structure is::

   https://beta.mybinder.org/v2/gh/<org-name>/<repo-name>/<branch|commit|tag>?filepath=<path/to/notebook.ipynb>

Share this link with anyone (i.e. colleagues, students) who would like to use
your Binder.

What technology does Binder use?
--------------------------------

Binder combines several open-source technologies, especially:

* `repo2docker <https://repo2docker.readthedocs.org>`_, for quickly generating
  Docker images from a GitHub repository.
* `JupyterHub <https://z2jh.jupyter.org>`_, for connecting a built Docker
  image to cloud computation and a user-facing web portal.
* `BinderHub <https://binderhub.readthedocs.org>`_, for gluing the above two
  tools together to create the Binder experience.

Tips for ensuring reproducibility with Binder
---------------------------------------------

Binder will create a new Docker image the first time is run with a repository.
From then on, a new image will only be created if the commit hash changes
(if you're linking Binder to a branch and not a specific commit hash). Here
are some tips to ensure reproducibility of your Binder links even if you must
re-build your repository image:

Pin your dependencies
`````````````````````

When you install a dependency, include its version number (depending on the
language you use, the exact syntax may vary). E.g., don't just specify ``numpy``,
specify ``numpy==1.12.0``.

``pip freeze`` is a handy tool to export the exact version of every Python
package in your environment in a format that can be used in ``requirements.txt``.

``conda env export -n <env-name>`` is the equivalent for anaconda's environment.yml
file.

Using Dockerfiles
`````````````````

Ensuring reproducibility with Dockerfiles comes with its own set of challenges.
For more information and best-practices when using Dockerfiles for Binder,
see :ref:`dockerfiles`.

What can I do if ``mybinder.org`` does not meet my needs?
---------------------------------------------------------

``mybinder.org`` uses software called ``BinderHub`` to carry out its services.
This is an Open Source, community-driven project that can be deployed on
most cloud providers. If you desire more computational resources for users or
want guaranteed uptime, consider setting up your own BinderHub deployment.

For more information, see the `BinderHub <https://binderhub.readthedocs.io/en/latest/>`_
documentation for instructions on how to deploy your own BinderHub, and the
`Zero to JupyterHub <https://zero-to-jupyterhub.readthedocs.io/en/latest/user-experience.html#set-user-memory-and-cpu-guarantees-limits>`_
documentation for how to customize the user environment.
