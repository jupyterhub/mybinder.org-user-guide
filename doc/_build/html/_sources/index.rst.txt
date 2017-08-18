Binder Documentation
====================

.. image:: https://badges.gitter.im/jupyterhub/binder.svg
   :alt: Join the chat at https://gitter.im/jupyterhub/binder
   :target: https://gitter.im/jupyterhub/binder?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Binder allows you to create custom computing environments that
can be shared and used by many remote users. This page provides information for those who wish to use a pre-existing
Binder deployment (e.g., ``mybinder.org``). If you'd like to create your own
Binder deployment, see the `BinderHub documentatoin <binderhub.readthedocs.org>`_.

What can I do with Binder?
--------------------------

Binder makes it simple to generate reproducible computing environments from
a GitHub repository. You can do this by putting two things into your repo:

* A collection of Jupyter Notebooks. These will be made available to users
  who navigate to your Binder repo.
* One (or many) text files that specify the requirements of your code. For example,
  a ``requirements.txt`` or ``environment.yml`` file. See the `repo2docker <repo2docker.readthedocs.org>`_
  documentation for a list of all the files and environments that are supported.

Binder uses the BinderHub technology to generate a Docker image from this
repository. The image will have all the components that you specify along with
the Jupyter Notebooks inside. You will be able to share a URL with users that
can immediately begin interacting with this environment via the cloud.

How can I generate a Binder repository?
---------------------------------------

All you need to do is put the files specified above into a GitHub repository.
Once that's done, navigate to ``beta.mybinder.org`` and insert the URL for
your git repository. Press ``Launch``, and your Binder will automatically be
created. When this is finished you will be automatically sent to a live
Jupyter session connected to this repository.

.. note::

   If a previous version of the repository has already been built, Binder will
   only build a new one if the git hashes don't match. If Binder *doesn't* have to build
   a new repository, the process of connecting to the live computational environment
   is *much* faster.

How can I generate Binder links?
--------------------------------

You may also specify a link that directly generates the Binder process. Here
is the structure to use::

   beta.mybinder.org/v2/gh/<org-name>/<repo-name>/<branch|commit|tag>?filepath=<path/to/notebook.ipynb>

What technology does Binder use?
--------------------------------
Binder combines several pieces of open-source technology, especially:

* `repo2docker <https://repo2docker.readthedocs.org>`_, for quickly generating Docker
  images from a GitHub repository.
* `JupyterHub <https://z2jh.jupyterhub.org>`_, for connecting a built Docker
  image to cloud computation and a user-facing web portal.
* `BinderHub <https://binderhub.readthedocs.org>`_, for gluing the above two tools
  together to create the Binder experience.
