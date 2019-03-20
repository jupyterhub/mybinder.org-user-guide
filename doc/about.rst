.. _about:

======================
About ``mybinder.org``
======================

mybinder.org is a deployment of the BinderHub technology. It is run as a public
service for those who'd like to share their interactive repositories publicly.
It is used by the Binder project to demonstrate the "cutting edge" of its technology.

This page explains some of the teams and organizations behind mybinder.org.

What kind of an organization is the Binder Project?
===================================================

The Binder Project is currently housed as a member of Project Jupyter, which is
itself housed under NumFocus, a 501c3 non-profit. 

Who runs mybinder.org?
======================

Currently, mybinder.org is run by the `Binder team <https://jupyterhub-team-compass.readthedocs.io/en/latest/team.html#binder-team>`_,
which are the core team members of the Binder Project.

Who pays for mybinder.org?
==========================

Currently, the BinderHub deployment at mybinder.org is funded with 
grants from the `Moore Foundation <https://figshare.com/s/e9d0ad7bdc4e405cccfa>`_.
and the `Google Cloud Platform <https://cloud.google.com/>`_.

What technology runs mybinder.org?
==================================

The technology behind mybinder.org is primarily composed of three open-source projects:

* `JupyterHub <https://z2jh.jupyter.org>`_, which manages cloud infrastructure for user instances
* `repo2docker <https://repo2docker.readthedocs.io>`_, which builds Docker images from GitHub repositories
* `BinderHub <https://binderhub.readthedocs.io>`_, which orchestrates the above two projects and
  provides the Binder interface.

Each of these are open and inclusively-governed projects. Currently, these are all officially
hosted as a part of `Project Jupyter <https://github.com/jupyter/governance>`_,
an open project that creates open tools for data science
infrastructure and interactive computation. The Binder team is
heavily involved in each.
