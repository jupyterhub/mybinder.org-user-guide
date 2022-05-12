#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path as op
from pathlib import Path
import requests

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_design",
    "sphinxext.rediraffe",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:

source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Binder"
copyright = "2017, The Binder Team"
author = "The Binder Team"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.1b"
# The full version, including alpha/beta/rc tags.
release = "0.1b"

intersphinx_mapping = {
    "r2d": ("https://repo2docker.readthedocs.io/en/latest/", None),
    "tc": ("https://jupyterhub-team-compass.readthedocs.io/en/latest/", None),
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Binder Logo
html_logo = "_static/images/logo.png"
html_favicon = "_static/images/favicon.png"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "use_edit_page_button": True,
    "google_analytics_id": "UA-101904940-3",
    "github_url": "https://github.com/jupyterhub/binder",
    "twitter_url": "https://twitter.com/mybinderteam",
    "icon_links": [
        {
            "name": "Go to mybinder.org",
            "url": "https://mybinder.org",
            "icon": "_static/favicon.png",
            "type": "local",
        }
   ],
   "navbar_end": ["navbar-icon-links", "support-button"],
}

html_context = {
    "github_user": "jupyterhub",
    "github_repo": "binder",
    "github_version": "master",
    "doc_path": "doc",
    "source_suffix": source_suffix,
}

html_sidebars = {
    "index": [],  # Remove sidebars on landing page to save space
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]

rediraffe_redirects = {
    "about.rst": "about/index.md",
    "contribute.md": "about/support.md",
    "examples.rst": "examples/examples.md",
    "index-repo-reference.rst": "examples/index.rst",
    "sample_repos.md": "examples/sample_repos.md",
    "index-community.rst": "about/index.md",
    "index-getting-started.rst": "introduction.md",
    "reliability.rst": "about/status.rst",
    "status.rst": "about/status.rst",
    "user-guidelines.rst": "about/user-guidelines.md",
    "using.rst": "using/using.rst",
}

# -- MyST Configuration ------------------------------------------
# See https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html#definition-lists
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Binderdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "Binder.tex", "Binder Documentation", "The Binder Team", "manual"),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "binder", "Binder Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Binder",
        "Binder Documentation",
        author,
        "Binder",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Scripts --------------------------------------------------------------
from subprocess import run
import shlex

# Update pages with source files stored on repo2docker
run(shlex.split(f"python _data/scripts/load_pages_from_r2d.py"))

# Generate snippets for federation/support
run(shlex.split(f"python _data/scripts/gen_federation_md.py"))
run(shlex.split(f"python _data/scripts/gen_support_md.py"))
