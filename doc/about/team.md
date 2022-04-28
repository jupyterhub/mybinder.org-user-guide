# Our team and tools

This page contains basic information about the people and tools behind the Binder service.

(team:members)=
## The Binder Team

The Binder Team is a subset of the {external+tc:doc}`JupyterHub Core Team <team>`.
This group builds and maintains our open source projects, operates the cloud infrastructure at mybinder.org, and broadly supports the mission of the Binder project for the communities we serve.

The service at `mybinder.org` is powered by a collection of BinderHub
deployments called {doc}`The BinderHub Federation <federation>` and run by a subset of the [Binder Team](team:members).

:::{button-ref} contribute
:ref-type: doc
:color: primary

Join our team
:::


## Our open source projects

The Binder Project stewards many open source projects that are particularly relevant to running BinderHub services like mybinder.org.
Below is a short list of the most relevant ones.

- [**BinderHub**](https://binderhub.readthedocs.io/): A distribution of [JupyterHub for Kubernetes](https://z2jh.jupyter.org) that dynamically builds user environment images and runs a Binder service for users. mybinder.org is an example of a live BinderHub deployment. 
- [**repo2docker**](https://repo2docker.readthedocs.io/): A tool for generating Docker images that serve interactive computing sessions backed by an environment the user defines. This tool is used by BinderHub to generate the images that users interact with.
- [**JupyterHub**](https://jupyterhub.readthedocs.io/): A flexible and scalable tool for providing remote access to Jupyter sessions on shared infrastructure. BinderHub is a customized and enhanced JupyterHub that runs on Kubernetes.

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

:::{grid-item-card} "Open in Binder"
:link: https://carreau.github.io/posts/32-open-with-binder-chrome/

A chrome extension to open a git repository in Binder.
From [Matthias Bussonier](https://carreau.github.io).
+++
Learn more {fas}`arrow-right`.
:::
::::
