.. _external_binder_setup:

======================================================
Use different repositories for content and environment
======================================================

Separating your Binder setup files from your repository content can be useful for a variety of reasons. Maybe they need different access permissions or you manage your working environment external to your code repository. Whatever the reason, with a custom Binder URL you can store your environment independent of your content.

The form on the `mybinder.org <https://mybinder.org>`_ home page only allows you to select a repository branch to build from. To create a BinderHub deployment link for situations where the environment and content are housed in separate repositories or on different branches of the same repository, you can use the `nbgitpuller link generator <https://jupyterhub.github.io/nbgitpuller/link?tab=binder>`_ to generate a formatted URL. Note that `nbgitpuller <https://github.com/jupyterhub/nbgitpuller>`_ must be included in your hub environment for this to work.

For some background on this how-to guide, see `this community forum post <https://discourse.jupyter.org/t/improve-documentation-for-new-users-not-working-on-the-master-branch/5509>`_. `Here <https://github.com/ICESAT-2HackWeek/2020_ICESat-2_Hackweek_Tutorials>`_ is an example repository using a JupyterHub environment configuration stored in a `separate repository <https://github.com/ICESAT-2HackWeek/jupyter-image-2020>`_. The environment was set up for a community workshop and the tutorial content was compiled and released after the workshop.
