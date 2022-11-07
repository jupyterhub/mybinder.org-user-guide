"""A nox configuration file so that we can build the documentation easily with nox.
- see the README.md for information about nox.
- ref: https://nox.thea.codes/en/stable/
"""
import nox
from pathlib import Path

nox.options.reuse_existing_virtualenvs = True


@nox.session
def docs(session):
    session.install("-r", "doc/doc-requirements.txt")
    session.run("sphinx-build", "-b=html", "doc/", "doc/_build/html")


@nox.session(name="docs-live")
def docs_live(session):
    session.install("-r", "doc/doc-requirements.txt")
    session.install("sphinx-autobuild")
    session.run(
        "sphinx-autobuild",
        "--re-ignore",
        "doc/_data*",
        "-b=html",
        "doc/",
        "doc/_build/html",
    )
