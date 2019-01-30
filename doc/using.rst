.. _using-binder:

===============================
Common usage patterns in Binder
===============================

This page describes some common patterns and use-cases for Binder.
If you're new to Binder, we recommend checking out :ref:`introduction`
for an introduction to Binder, repository structure, and how to build your
own repository.

For a more complete list of sample repositories for use with Binder, see the
`Sample Binder Repositories <sample_repos.html>`_ page.

Choose from many open source languages
======================================

Binder runs on JupyterHub, a language-agnostic tool for serving data
analytics sessions in the cloud. This means that you can build Binders
using many popular open source languages.

For example, here's a short list of Binder repositories that are built
with several popular languages:

* Python
    * `A simple pip environment <https://github.com/binder-examples/requirements>`_.
    * `An Anaconda Python environment <https://github.com/binder-examples/conda>`_.
* R
    * `Using R, RStudio, and Shiny <https://github.com/binder-examples/r>`_.
* Julia
    * `A simple Julia repository <https://github.com/binder-examples/julia-python>`_.

You can also control the versions used for each of these languages. For
more information about this, see the :ref:`config-files` page.

Choose from multiple user interfaces
====================================

Binder is also agnostic to the specific user interface that you'd like
to share with your Binder. BinderHub will make some assumptions about the
interface you'd like depending on the environment you specify (for example,
if you use Python and have Jupyter Notebooks in the repository, Binder
will use a notebook interface for links). However, you can configure Binder
to use whatever interface you'd like.

For example, here are a few repositories demonstrating different user
interfaces.

* `The Classic Notebook interface <https://github.com/binder-examples/python-conda_pip>`_
* `Jupyter Lab <https://github.com/jupyterlab/jupyterlab-demo>`_
* `The nteract interface <https://mybinder.org/v2/gh/nteract/examples/master?urlpath=%2Fnteract%2Fedit%2Fpython%2Fintro.ipynb>`_
* `RStudio sessions <https://github.com/binder-examples/r>`_

For a more complete description of the interfaces people have used
with Binder, see :ref:`user_interface`.


Creating live demonstrations
============================

Binder is useful if you want to interactively demonstrate something to
a group of people, and would like them to immediately interact with the
material as well.

There are several tools that make it easy to show off computational ideas
and narratives. For example, you can build a Binder that is powered
by Jupyter Notebooks, or turn them into an `interactive presentation with RISE <https://github.com/binder-examples/jupyter-rise>`_.

If you're using Binder for a presentation, demo, or tutorial, just make
sure that you've built the latest version of your Binder *before* you share
a link with your audience to ensure that the build process has completed.


Share computational work with Binder
====================================

Another common use for Binder is to use Binder to quickly show off your
data science work. For example, if you'd like to share some analyses and
visualizations on a dataset of interest. In this case, it is common
to "prepare" your Binder for the analysis. For example,
by downloading and modifying some data.

Binder allows you to run an arbitrary
script *after* the environment has been installed. This is accomplished
with a **``postBuild``** file. It will be run from the shell.

The Docker image for the repository will be run **after** the ``postBuild``
script has finished, meaning that the state of the repository will be baked
into the image itself. Be careful - this means that if you download a 10GB
dataset, you'll have at least a 10GB Docker image for your repository.

Another common task is to ensure some code is run just before users begin
their session. You can accomplish this with a **``start``** configuration file.
This file will be run **just before an interactive session begins**. It will
not be baked into your Binder's Docker image.

Use Binder in educational courses
=================================

Binder gives users quick, interactive experiences with computational
material that you provide. This can be useful in a teaching context, where
you'd like students to quickly dive-in to the work you are covering.

It is beyond the scope of the Binder documentation to cover the many
ways that Binder can be used in an educational context. We recommend
checking out the `Jupyter for Education guide <https://jupyter4edu.github.io/jupyter-edu-book/>`_
for a collection of information about creating courses with open source content,
including how to incorporate Binder into your course.

For more information about all of the things you can do with Binder, see
the :ref:`config-files` page or see the whole :ref:`binder-docs`.
