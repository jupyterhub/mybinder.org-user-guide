"""A nox configuration file so that we can build the documentation easily with nox.
- see the README.md for information about nox.
- ref: https://nox.thea.codes/en/stable/
"""
import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", "doc", "doc/_build/html"]

@nox.session(python="3.12")
def docs(session):
    session.install("-r", "doc/doc-requirements.txt")
    if "live" in session.posargs:
        AUTOBUILD_IGNORE = [
            "*/.github/*",
            "*/_data/*",
            "*/howto/languages.rst",
            "*/howto/user_interface.rst",
            "*/howto/lab_workspaces.rst",
            "*/using/config_files.rst",
        ]
        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])
        cmd.extend(build_command)
        session.run(*cmd)
    else:
        session.run("sphinx-build", *build_command)
