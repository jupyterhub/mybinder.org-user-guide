.. _using-binder:

================
Common use-cases
================

This page describes some common patterns and use-cases for Binder.
If you're new to Binder, we recommend checking out :ref:`introduction`
for an introduction to Binder, repository structure, and how to build your
own repository.

For a more complete list of sample repositories for use with Binder, see the
`Sample Binder Repositories <sample_repos.html>`_ page.


Creating live demonstrations
============================

Binder is useful if you want to interactively demonstrate something to
a group of people, and would like them to immediately interact with the
material as well.

There are several tools that make it easy to show off computational ideas
and narratives. For example, you can build a Binder that is powered
by Jupyter Notebooks, or turn them into an `interactive presentation with RISE <https://github.com/binder-examples/jupyter-rise>`_.

If you're using Binder for a presentation, demo, or tutorial, just make
sure that you've built the latest version of your Binder repository *before*
you share a link with your audience to ensure that the build process has
completed.


Share computational work or papers
==================================

Another common use for Binder is to use Binder to quickly show off your
data science work. For example, if you'd like to share some analyses and
visualizations on a dataset of interest. In this case, it is common
to "prepare" your Binder repository for the analysis. For example,
by downloading and modifying some data.

Binder allows you to run an arbitrary
script *after* the environment has been installed. This is accomplished
with a ``postBuild`` file. It will be run from the shell.

The Docker image for the repository will be run **after** the ``postBuild``
script has finished, meaning that the state of the repository will be baked
into the image itself. Be careful - this means that if you download a 10GB
dataset, you'll have at least a 10GB Docker image for your repository.

Another common task is to ensure some code is run just before users begin
their session. You can accomplish this with a ``start`` configuration file.
This file will be run **just before an interactive session begins**. It will
not be baked into your Binder repository's Docker image.

Sharing course content and educational material
===============================================

Binder gives users quick, interactive experiences with computational
material that you provide. This can be useful in a teaching context, where
you'd like students to quickly dive-in to the work you are covering.

It is beyond the scope of the Binder documentation to cover the many
ways that Binder can be used in an educational context. We recommend
checking out the `Jupyter for Education guide <https://jupyter4edu.github.io/jupyter-edu-book/>`_
for a collection of information about creating courses with open source content,
including how to incorporate Binder into your course.

Generating interactive open-source package documentation
========================================================

Binder is a useful resource for those who are developing packages
in an open source language such as Python, Julia, or R. It's important
to give users the ability to quickly interact with features, APIs,
and tutorials that teach people how (and why) to use a package.

Binder is useful for generating quick, interactive experiences that
serve this purpose. For example, `Sphinx-Gallery <https://sphinx-gallery.github.io>`_ allows you to
build documentation from Python examples and create a visual gallery
for each. It can `automatically create Binder links <https://sphinx-gallery.github.io/configuration.html?highlight=binder#binder-links>`_
for each page. In addition, the R community has a tool called
`holepunch <https://github.com/karthik/holepunch>`_ that helps you quickly
generate binder-ready repositories for R workflows.

For more information about all of the things you can do with Binder, see
the :ref:`config-files` page or see the whole :ref:`binder-docs`.
