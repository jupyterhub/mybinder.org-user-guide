================================
Frequently Asked Questions (FAQ)
================================

mybinder.org is a deployment of the BinderHub technology. It is run as a public
service for those who'd like to share their interactive repositories publicly.
It is used by the Binder project to demonstrate the "cutting edge" of its technology.

This page explains some of the teams and organizations behind mybinder.org, as
well as common questions about using mybinder.org

.. _about:

About ``mybinder.org``
======================

Information about the Binder service at ``mybinder.org`` and the teams behind it.

.. _about-binder-project:

What is the Binder Project?
---------------------------

The Binder Project is an open community that makes it possible to create sharable,
interactive, reproducible environments. The main technical product that
the community creates is called BinderHub, which you can try out
at `mybinder.org`. 

The Binder Project is currently housed as a member of Project Jupyter, which is
itself housed under NumFocus, a 501c3 non-profit. 

.. _citing:

How can I cite Binder?
----------------------

If you publish work that uses Binder, please consider citing the
`Binder paper from the 2018 SciPy proceedings <http://conference.scipy.org/proceedings/scipy2018/project_jupyter.html>`_!

Here is a citation that you can use:

.. code-block::

   Jupyter et al., "Binder 2.0 - Reproducible, Interactive, Sharable
   Environments for Science at Scale." Proceedings of the 17th Python
   in Science Conference. 2018. doi://10.25080/Majora-4af1f417-011

https://doi.org/10.25080/Majora-4af1f417-011


Who runs mybinder.org?
----------------------

The service at ``mybinder.org`` is powered by a collection of BinderHub
deployments called :doc:`The BinderHub Federation <federation>` and run by
the `Binder team <https://jupyterhub-team-compass.readthedocs.io/en/latest/team.html#binder-team>`_.

For more information about the BinderHubs behind ``mybinder.org``, see
:doc:`The BinderHub Federation <federation>`.

Who supports mybinder.org?
--------------------------

See :doc:`support`.

What technology runs mybinder.org?
----------------------------------

The technology behind mybinder.org is primarily composed of three open-source projects:

* `JupyterHub <https://z2jh.jupyter.org>`_, which manages cloud infrastructure for user instances
* `repo2docker <https://repo2docker.readthedocs.io>`_, which builds Docker images from GitHub repositories
* `BinderHub <https://binderhub.readthedocs.io>`_, which orchestrates the above two projects and
  provides the Binder interface.

Each of these are open and inclusively-governed projects. Currently, these are all officially
hosted as a part of `Project Jupyter <https://github.com/jupyter/governance>`_,
an open project that creates open tools for data science
infrastructure and interactive computation. The Binder team is
heavily involved in each.

Using the ``mybinder.org`` service
==================================

Information about using the ``mybinder.org`` service.

Check out :doc:`user-guidelines` for more information about using ``mybinder.org``.

Is ``mybinder.org`` free to use?
--------------------------------

Yes! Though note that it has :ref:`limited computational resources
<user_memory>`.

.. _user_memory:

How much memory am I given when using Binder?
---------------------------------------------

If you or another Binder user clicks on a Binder link, the ``mybinder.org``
deployment will run the linked repository. While running, users are guaranteed
*at least* 1GB of RAM, with a *maximum* of 2GB. This means you will always have
1GB, you may occasionally have between 1 and 2GB, and if you go over 2GB your kernel
will be restarted.

How long will my Binder session last?
-------------------------------------

Binder is meant for interactive and ephemeral interactive coding, meaning that
it is ideally suited for relatively short sessions. Binder will automatically
shut down user sessions that have more than 10 minutes of inactivity
(if you leave a jupyterlab window open in the foreground,
this will generally be counted as "activity").

Binder aims to provide up to six hours of session time per user session,
or up to one cpu-hour for more computationally intensive sessions.
Beyond that, we cannot guarantee that the session will remain running.

How much does running ``mybinder.org`` cost?
--------------------------------------------

Great question! If you're interested in the technical costs of running
``mybinder.org``, we publish a semi-up-to-date dataset of our costs at the
`binder-data <https://github.com/jupyterhub/binder-data/tree/master/billing/data/proc>`_
repository. In addition, you can explore these costs with the binder link below!

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/jupyterhub/binder-billing/master?urlpath=lab/tree/analyze_data.ipynb

How can ``mybinder.org`` be free to use?
----------------------------------------

See :ref:`about` for more information on the mybinder.org team and who provides
the resources to pay for the service. Generally, mybinder.org is run with modest resources
provided to users in order to keep costs down. In the future we hope to see more
public BinderHub services running that can form a collection of community
resources for interactive cloud computing.

Can I use mybinder.org for a live demo or workshop?
---------------------------------------------------

For sure! We hope the demo gods are with you. Please do make sure you have a
backup plan in case there is a problem with mybinder.org during your workshop
or demo. Occasionally, service on ``mybinder.org`` can be degraded, usually because
the server is getting a lot of attention somewhere on the
internet, because we are deploying new versions of software, or the team
can't quickly respond to an outage.

Check out :doc:`user-guidelines` for more information about using ``mybinder.org``.

How does mybinder.org ensure user privacy?
------------------------------------------

We take user privacy very seriously! Because Binder runs as a public,
free service, we don't require any kind of log-in that would let us
keep track of user data. All code that is run, data analyzed, papers
reproduced, classes taught - in short, everything that happens in a
Binder session - is destroyed when the user logs off or becomes inactive
for more than a few minutes.

Here are the pieces of information we do keep: We run google analytics
with anonymized IPs and no cookies, which gives us just enough information
to know how Binder is being used, and but won't be able to identify users.
We also retain logs of IP addresses for 30 days, which is used solely in
the case of detecting abuse of the service. If you have suggestions for
how we can ensure the privacy of our data and users, we'd love to hear it!

How secure is mybinder.org?
---------------------------

The Binder team has put in a lot of work to ensure that the mybinder.org
service runs as secure as possible. However, it is a free, public service
that is open to the world, and **you should never share sensitive or personal
information within a Binder repository**. This includes passwords, data that
shouldn't be public, API keys, etc.

You should ensure that sensitive information doesn't make it into the built
docker image for your Binder repository (aka, that it isn't used in one of your
configuration files) and that you don't use this information from within
a Binder session (e.g. hard-coding an API key into an HTTP request that you
call from a Jupyter Notebook).

If you require private information within your
Binder instance, consider `deploying a BinderHub for your group <https://binderhub.readthedocs.io/en/latest/>`_.

Where can I report a security issue?
------------------------------------

If you find a security vulnerability in with ``mybinder.org``, please report
it to `security@ipython.org <security@ipython.org>`_.

If you prefer to encrypt your security reports, you can use `this PGP public key
<https://jupyter-notebook.readthedocs.io/en/stable/_downloads/ipython_security.asc>`_.

Can I push data from my Binder session back to my repository?
-------------------------------------------------------------

While it is *technically* possible to push information from a Binder
session onto a platform like GitHub, we *strongly discourage* it. We
cannot guarantee the security of data moving through ``mybinder.org``,
and your password or any sensitive data may be compromised. You
shouldn't do anything on ``mybinder.org`` that you wouldn't mind sharing
with the world!

Can I put my configuration files outside the root of my repository?
-------------------------------------------------------------------

Yes! Configuration files may be placed in the root of your repository or
in a ``binder/`` folder in the root of your repository (i.e. ``myproject/binder/``).
If a ``binder/`` folder is used, Binder will only read configuration files
from that location (i.e. ``myproject/binder/requirements.txt``) and will
ignore those in the repository's root (``myproject/environment.yml`` and
``myproject/requirements.txt``).

What factors influence how long it takes a Binder session to start?
-------------------------------------------------------------------

Understanding why some operations take longer than others requires a very
brief overview of the pieces of machinery at play with BinderHub. There two
things worth mentioning:

* A *user pod* is the virtual machine that runs a users' code.
* A *node* is the machine, running in the cloud, where a bunch of pods live.
  There are many nodes for a Binder server, depending on the number of people
  using the service.
* A *registry* is a service in the cloud where Docker images are stored. BinderHub
  has the ability to push / pull from this registry, which it uses to
  manage Binder environment images.

With that being said, there are three primary things that need to happen any
time someone clicks a Binder link.

1. A Docker image for the link must exist in Binder's image registry. If an image
   for the current ``ref`` of the repository *doesn't* exist, one will be built
   and registered automatically using ``repo2docker``. If your
   configuration files specify a large or complex environment, this will take
   some time while your image builds.
2. The Docker image must exist on the node that the user will use. If it does not,
   then BinderHub will pull the image. If the image is large, this will
   take some time depending on the server load and image size.
3. A pod for the user must be created to serve this Docker image. This usually
   happens in seconds, though may take longer if the server is under a heavy
   load.

These three things happen in a nested fashion. "3" always happens, "2" only
happens the *first* time a node is used to serve a particular Docker image, "1"
only happens the first time someone clicks a Binder link for a repository with
an updated ``ref``. They take roughly decreasing amounts of time to complete,
so 1 >> 2 >> 3 in terms of how long each operation takes.

If Binder sessions take a while to start, but you know that your image has
already been built, there's a good chance you are in step 2, and the server is
still pulling the image onto the node that you'll be using. Please be patient!

Will repos with fewer notebooks launch faster? Should I split my notebooks into smaller repos?
----------------------------------------------------------------------------------------------

Number of notebooks in a repo shouldn't have any impact on binder launch time,
assuming a docker image for that repo is already built. It is worth noting, however,
that there is a limit to the number of instances of a repository that can be active
at any moment in time.

Will repos that are launched often get prioritized and launch faster?
---------------------------------------------------------------------

There isn't any intentional prioritization for repos that are launched frequently,
however, in practice the repos that launch more often will tend to launch faster.
This is because if a user pod is put on a node that doesn't already have the Docker
image for that repo, then it'll have to do a Docker pull first, which takes time. If
a repo is launched a lot, then most likely it will already be on a given node.

What can I do if ``mybinder.org`` does not meet my needs?
---------------------------------------------------------

``mybinder.org`` uses software called `BinderHub`_ to carry out its services.
This is an Open Source, community-driven project that can be deployed on
most cloud providers. If you desire more computational resources for users or
want guaranteed uptime, consider setting up your own BinderHub deployment.

For more information, see the `BinderHub documentation <BinderHub_>`_
for instructions on how to deploy your own BinderHub, and the
`Zero to JupyterHub <https://zero-to-jupyterhub.readthedocs.io/en/latest/user-experience.html#set-user-memory-and-cpu-guarantees-limits>`_
documentation for how to customize the user environment.


Other tools in the Binder ecosystem
-----------------------------------

.. card::
   :text-align: center

   Google Chrome extension:
   `Open in Binder <https://carreau.github.io/posts/32-open-with-binder-chrome.html>`_.
   +++
   `Matthias Bussonier <https://carreau.github.io>`_.

