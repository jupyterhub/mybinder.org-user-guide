Using a Dockerfile
------------------

Binder supports configuration files for package
installation, environment specification, post-build shell scripts, and more.
It should be possible to create the environment that you want *without*
using a Dockerfile. For more information about the different environment
configuration files that Binder can create, see the
`guide to creating Binder-ready repositories <LINK>`_.

However, in case you cannot meet all your needs with these configuration
files, it is also possible to use a Dockerfile to define your environment.
This is considered an **advanced use case**, and we cannot guarantee that the
Dockerfile will work.

This guide will help you in preparing your Dockerfile so that it has the
components needed to run JupyterHub, allowing it to work on Binder
deployments.

When should you use a Dockerfile?
=================================

Below are a few use-cases where you *might* want to use a Dockerfile with
Binder.

When you must inherit from a popular Docker image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use a pre-existing Docker image, you may source it in your
Dockerfile. For example, this code sources the Jupyter-Scipy notebook:

.. code-block:: Dockerfile

    # Note that there must be a tag
    FROM jupyter/scipy-notebook:cf6258237ff9

See `Preparing your Dockerfile <LINKTOPREPARING>`_ for instructions on how to
do this properly.

When you are building complex software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some software is simply too complex to be specified with Binder configuration
files. For example, if you need to *DO SOME COOL SHIT ADD EXAMPLES*.

When you're using a language that is not directly supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Binder supports many languages, but not all of them. If your need to use
a different language, it may be possible to accomplish this with a Dockerfile.

For a list of languages that Binder supports with configuration files, see
`LINK TO REPO2DOCKER OR SOMETHING <r2d>`_.

.. note::

   We welcome contributions to ``repo2docker`` to add support for new
   languages. If interested, please `open an issue <R2D LINK>`_.


Preparing your Dockerfile
=========================

For a Dockerfile to work on binder, it must meet the following requirements:

1. It must install JupyterHub.

   JupyterHub is what will serve your Docker image to users.
   This is installed via ``pip`` and the ``jupyterhub`` package.

   .. note::

      JupyterHub only works with Python 3. You need to have python 3 available
      in your environment in order to install it.

   The version of JupyterHub installed must match the version used by
   your Binder deployment. To ensure this, install it with the following code:

       .. code-block:: Dockerfile

          # NOTE: THIS DOES NOT ACTUALLY WORK RIGHT NOW, YOU HAVE TO DO ==0.7.2
          # LET'S FIX THAT
          RUN pip3 install --no-cache-dir jupyterhub=${JUPYTERHUB_VERSION}

2. It must explicitly specify a tag in the image you source.

   When sourcing a pre-existing Docker image with ``FROM``,
   **a tag is required**. The tag *cannot* be ``latest``.

   Here's an example of a Dockerfile ``FROM`` statement that would work:
   Do this:

   .. code-block:: Dockerfile

      FROM jupyter/scipy-notebook:cf6258237ff9

   .. note::

       These would **not** work:

       .. code-block:: Dockerfile

          FROM jupyter/scipy-notebook

       or

       .. code-block:: Dockerfile

          FROM jupyter/scipy-notebook:latest

3. It must copy its contents to the ``HOME`` directory and change permissions.

   To make sure that your repository contents are available to users,
   you must copy all contents to ``$(HOME)`` and then make this folder
   owned by users. You can accomplish this by putting the following lines
   into your Dockerfile:

   .. code-block:: Dockerfile

       # Make sure the contents of our repo are in ${HOME}
       COPY . ${HOME}
       USER root
       RUN chown -R ${NB_USER}:${NB_USER} ${HOME}
       USER ${NB_USER}

   This is required because Docker will be default
   set the owner to ``ROOT``, which would prevent users from editing files.
