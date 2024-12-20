#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- General configuration ------------------------------------------------
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
main_doc = "index"

# General information about the project.
project = "Binder"
copyright = "2022, The Binder Team"
author = "The Binder Team"
version = "0.1b"
# The full version, including alpha/beta/rc tags.
release = "0.1b"

intersphinx_mapping = {
    "r2d": ("https://repo2docker.readthedocs.io/en/latest/", None),
    "tc": ("https://jupyterhub-team-compass.readthedocs.io/en/latest/", None),
}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

# -- Options for HTML output ----------------------------------------------
html_theme = "pydata_sphinx_theme"
html_favicon = "_static/images/favicon.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "use_edit_page_button": True,
    "analytics": {
        "google_analytics_id": "UA-101904940-3",
    },
    "icon_links": [
        {
            "name": "Go to mybinder.org",
            "url": "https://mybinder.org",
            "icon": "_static/favicon.png",
            "type": "local",
        },
        {
            "name": "GitHub repository",
            "url": "https://github.com/jupyterhub/binder",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter account",
            "url": "https://twitter.com/mybinderteam",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "Community Forum",
            "url": "https://discourse.jupyter.org/c/binder/12",
            "icon": "fa-brands fa-discourse",
        },
    ],
    "navbar_align": "left",
    "navbar_end": ["theme-switcher", "navbar-icon-links", "support-button"],
    "logo": {
        "image_light": "_static/images/logo.png",
        "image_dark": "_static/images/logo-dark.png",
    },
}

html_context = {
    "github_user": "jupyterhub",
    "github_repo": "binder",
    "github_version": "main",
    "doc_path": "doc",
    "source_suffix": source_suffix,
}

html_sidebars = {
    "index": [],  # Remove sidebars on landing page to save space
}
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

# -- Scripts --------------------------------------------------------------
from subprocess import run
import shlex

# Update pages with source files stored on repo2docker
run(shlex.split(f"python _data/scripts/load_pages_from_r2d.py"))

# Generate snippets for federation/support
run(shlex.split(f"python _data/scripts/gen_federation_md.py"))
run(shlex.split(f"python _data/scripts/gen_support_md.py"))
