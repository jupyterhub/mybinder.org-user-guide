(binder-docs)=
# Binder Documentation

```{div} badges
[![Join the chat at https://gitter.im/jupyterhub/binder](https://badges.gitter.im/jupyterhub/binder.svg)](https://gitter.im/jupyterhub/binder)

[![Join our community Discourse page at https://discourse.jupyter.org](https://img.shields.io/discourse/https/discourse.jupyter.org/users.svg?colorB=blue&label=discourse&style=flat)](https://discourse.jupyter.org)
```

<br />

**Binder** allows you to create custom computing environments that can be shared
and used by many remote users.

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} {fas}`bolt;sd-text-warning` Get started
:link: introduction
:link-type: doc

Our getting started section helps you create and launch your first repository on mybinder.org.
+++
Learn more {fas}`arrow-right`
:::

:::{grid-item-card} {fas}`lightbulb;sd-text-primary` Learn more
:link: howto/index
:link-type: doc

Our how-to guides have a collection of snippets and a short overview of useful ways to use Binder.
+++
Learn more {fas}`arrow-right`
:::

:::{grid-item-card} {fas}`heart;sd-text-danger` Support Binder
:link: about/support
:link-type: doc

The Binder Project is a non-profit project built, led, and supported by an open community.
Click here for some ideas on how to support the project.
+++
Learn more {fas}`arrow-right`
:::

:::{grid-item-card}
:columns: 12 
:link: about/supporters
:link-type: doc
:text-align: center

{octicon}`heart-fill;2em;sd-text-danger` **Thanks to our supporters** {octicon}`heart-fill;2em;sd-text-danger`
:::

::::



## What is Binder?

A Binder service is powered by [BinderHub](https://github.com/jupyterhub/binderhub),
an open-source tool that runs on Kubernetes.
One such deployment lives at [mybinder.org](https://mybinder.org), and is free to use.

:::{admonition} Other documentation in the Binder ecosystem
:class: tip
This documentation is for creators of Binder repositories, and those who wish to use
and learn more about the service at `mybinder.org`. You may be interested in the following
other documentation sites:

👉 [the BinderHub documentation](https://binderhub.readthedocs.io)
: Has information about deploying your own BinderHub in the cloud. It is meant for people that wish to replicate the `mybinder.org` service at a different location for their community.

👉 [the mybinder.org site-reliability guide](https://mybinder-sre.readthedocs.io)
: Has information for the team running `mybinder.org`, including dev-ops best-practices and tips for running the BinderHubs behind `mybinder.org`.

👉 [the JupyterHub team compass docs](https://jupyterhub-team-compass.readthedocs.io)
: Has team information, practices, and guides for the JupyterHub community. This is also a great resource if you're looking for ways to get involved!
:::

## Get started

To learn more about Binder, check out our tutorials, which will help you get started and learn more about sharing reproducible environments with Binder.

```{toctree}
:maxdepth: 2

tutorials/index
```

## How-To guides and Tutorials

The following sections discuss some more in-depth topics on preparing and sharing
your Binder repository. How-To guides are shorter, actionable patterns that
accomplish something specific. Tutorials are more high-level and thorough,
and often cover more conceptual topics.

```{toctree}
:maxdepth: 2

howto/index
```

## Reference information about Binder

```{toctree}
:maxdepth: 2

reference/index
```

## Information about `mybinder.org`

Information about using and running the Binder service at `mybinder.org`.

```{toctree}
:maxdepth: 2

about/index
```

See the [Binder Examples](https://github.com/binder-examples) GitHub
organization for more Binder repositories demonstrating its functionality.

## Cite Binder

For information on how to cite Binder, see [](about:citing).
