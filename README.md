# binder

[![Documentation Status](https://readthedocs.org/projects/mybinder/badge/?version=latest)](https://mybinder.readthedocs.io/en/latest/?badge=latest)
[![Join the chat at https://gitter.im/jupyterhub/binder](https://badges.gitter.im/jupyterhub/binder.svg)](https://gitter.im/jupyterhub/binder?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This repository contains the documentation and usage instructions for the mybinder.org service.

## Related Repositories

**For BinderHub, the open-source technology that runs mybinder.org, please visit [jupyterhub/binderhub](https://github.com/jupyterhub/binderhub)**

**For repo2docker, the open-source technology to turn Git repositories into Jupyter enabled Docker Images, please visit [jupyter/repo2docker](https://github.com/jupyter/repo2docker)**

 For deployment of the website [mybinder.org](https://mybinder.org), please
 visit [mybinder.org-deploy](https://github.com/jupyterhub/mybinder.org-deploy).  

BinderHub uses Helm to configure and manage deployment
of the Binder service. For details about this deployment, please visit [helm-chart](https://github.com/jupyterhub/helm-chart).  

## Maintainers

Binder is maintained by the [Binder team](https://github.com/jupyterhub/team-compass#binder-team).  Administration is managed at [team compass](https://github.com/jupyterhub/team-compass).


The JupyterHub team also maintains analysis of binder data including [billing data](https://github.com/jupyterhub/binder-billing) and [activity data](https://github.com/jupyterhub/binder-data).

## Build the documentation

This documentation is built with [the Sphinx Documentation engine]().
The easiest way to build the documentation is with [the tool `nox`](https://nox.thea.codes/en/stable/).
`nox` is kind-of like a Makefile, it is a way to automatically install environments and run commands locally.
To build this documentation with `nox`, run:

```bash
pip install nox
nox -s docs
```

or to launch a live server that re-builds and re-loads pages as you save files:

```bash
nox -s docs-live
```

Alternatively, you may build the documentation directly with Sphinx:

```bash
pip install -r doc/doc-requirements.txt
sphinx-build -b html doc doc/_build
```
