# Our team and tools

This page contains basic information about the people and tools behind the Binder service.

(team:members)=
## The Binder Team

The Binder Team is a subset of the {external:tc:ref}`JupyterHub Core Team <jupyterhub-team>`.
This group builds and maintains our open source projects, operates the cloud infrastructure at mybinder.org, and broadly supports the mission of the Binder project for the communities we serve.

The service at `mybinder.org` is powered by a collection of BinderHub
deployments called {doc}`The BinderHub Federation <federation>` and run by a subset of the [Binder Team](team:members).

The Binder Project is a sub-project of [Project Jupyter](https://jupyter.org), which is a fiscally-sponsored project of [NumFocus](https://numfocus.org), a 501c3 non-profit.

:::{button-ref} support:join
:color: primary

Join our team
:::

(support:partner-institutions)=
## Partner institutions

We appreciate the generosity of institutions that allow their team members to support the mybinder.org federation in an official capacity.
Below are institutions that employ individuals that operate any of the hubs in [the mybinder.org federation](federation.md).

Below are the current partner institutions of mybinder.org.

```{include} ../_data/snippets/supporters_partners_md.txt
```

(team:os-projects)=
## Our open source projects

The Binder Project stewards many open source projects that are particularly relevant to running BinderHub services like mybinder.org.
Below is a short list of the most relevant ones.

- [**BinderHub**](https://binderhub.readthedocs.io/) ([{fab}`github`](https://github.com/jupyterhub/binderhub)): A distribution of [JupyterHub for Kubernetes](https://z2jh.jupyter.org) that dynamically builds user environment images and runs a Binder service for users. mybinder.org is an example of a live BinderHub deployment. 
- [**repo2docker**](https://repo2docker.readthedocs.io/) ([{fab}`github`](https://github.com/jupyterhub/repo2docker)): A tool for generating Docker images that serve interactive computing sessions backed by an environment the user defines. This tool is used by BinderHub to generate the images that users interact with.
- [**JupyterHub for Kubernetes**](https://z2jh.jupyter.org) ([{fab}`github`](https://github.com/jupyterhub/zero-to-jupyterhub-k8s)): A distribution of JupyterHub that runs on the cloud- and vendor-agnostic cloud platform [Kubernetes](https://kubernetes.io). This version of JupyterHub is highly configurable and scalable, and is used in BinderHub's deployment.
- [**JupyterHub**](https://jupyterhub.readthedocs.io/) ([{fab}`github`](https://github.com/jupyterhub/jupyterhub)): A flexible and scalable tool for providing remote access to Jupyter sessions on shared infrastructure. BinderHub is a customized and enhanced JupyterHub that runs on Kubernetes.

Each of these are open projects led by an inclusive community.
These are all officially hosted as a part of [Project Jupyter](https://jupyter.org).

### Other tools in the Binder ecosystem

::::{grid} 3
:::{grid-item-card} Holepunch
:link: https://github.com/karthik/holepunch

A tool for quickly creating Binder-ready repositories in R.

+++
Learn more {fas}`arrow-right`.
:::

::::
