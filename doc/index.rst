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

See the `Binder Examples <https://github.com/binder-examples>`_ GitHub
organization for sample Binder repositories demonstrating its functionality.

Site contents
-------------

.. toctree::
   :maxdepth: 2

   dockerfile
   reproducibility
   sample_repos
   faq

What can I do with Binder?
--------------------------

Binder makes it simple to generate reproducible computing environments from a
Git repository. Binder uses the BinderHub technology to generate a Docker
image from this repository. The image will have all the components that you
specify along with the Jupyter Notebooks inside. You will be able to share a URL
with users that can immediately begin interacting with this environment via the
cloud.

.. _preparing_repositories:

Preparing a repository for Binder
---------------------------------

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

Generating a sharable Binder link
---------------------------------

You may share a link that generates a Binder. To generate a link for your
Binder repository, type in the URL of the repository in the Binder UI and
click the small carrot next to the ``Launch`` button. This will open a popup
where you can display and select the text for your link.

The link structure is::

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
