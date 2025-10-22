# Usage guidelines

This page details some guidelines and policies that we follow at ``mybinder.org``.

:::{admonition} When in doubt, open an issue
:class: warning
If you're not sure whether your use-case is reasonable for `mybinder.org`, don't
hesitate to [open an issue](https://github.com/jupyterhub/mybinder.org-deploy/issues/new?labels=question&template=repo_check.md)
to ask if your planned usage is OK.
:::

## Resources available

(user-memory)=
### How much memory am I given when using Binder?

If you or another Binder user clicks on a Binder link, the `mybinder.org`
deployment will run the linked repository. While running, users are guaranteed
*at least* 1GB of RAM, with a *maximum* of 2GB. This means you will always have
1GB, you may occasionally have between 1 and 2GB, and if you go over 2GB your kernel
will be restarted.

### How long will my Binder session last?

Binder is meant for interactive and ephemeral interactive coding, meaning that
it is ideally suited for relatively short sessions. Binder will automatically
shut down user sessions that have more than 10 minutes of inactivity
(if you leave a jupyterlab window open in the foreground,
this will generally be counted as "activity").

Binder aims to provide up to six hours of session time per user session,
or up to one cpu-hour for more computationally intensive sessions.
Beyond that, we cannot guarantee that the session will remain running.

### Maximum Concurrent Users for a Repository

We don't want a single repository to dominate all of the traffic to Binder, so
we've set a maximum limit of concurrent user sessions that point to the same
Binder link. **The maximum number of simultaneous users for a given repo is 100**.
If you think you have a *really* good reason for why this number should be
higher, please [Open an Issue](https://github.com/jupyterhub/mybinder.org-deploy/issues/new?labels=impact&template=request_resources.yml).
to discuss with the community!

### Events and workshops

If you'd like to run an event with `mybinder.org` and expect more than 100 users
to join at once, please [request an increase in quota for your repository](https://github.com/jupyterhub/mybinder.org-deploy/issues/new?labels=impact&template=request_resources.yml).

The Binder Team occasionally increases the number of sessions that can run for a single repository if it is being used for purposes that align with the mission of the Binder Project. However, there is no guarantee that this will be done for your event.

### What can I do if `mybinder.org` does not meet my needs?

`mybinder.org` uses software called [BinderHub] to carry out its services.
This is an Open Source, community-driven project that can be deployed on
most cloud providers. If you desire more computational resources for users or
want guaranteed uptime, consider setting up your own BinderHub deployment.

For more information, see the [BinderHub documentation][binderhub]
for instructions on how to deploy your own BinderHub, and the
[Zero to JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/user-experience.html#set-user-memory-and-cpu-guarantees-limits)
documentation for how to customize the user environment.

## Performance and speed


### What factors influence how long it takes a Binder session to start?

Understanding why some operations take longer than others requires a very
brief overview of the pieces of machinery at play with BinderHub. There two
things worth mentioning:

- A *user pod* is the virtual machine that runs a users' code.
- A *node* is the machine, running in the cloud, where a bunch of pods live.
  There are many nodes for a Binder server, depending on the number of people
  using the service.
- A *registry* is a service in the cloud where Docker images are stored. BinderHub
  has the ability to push / pull from this registry, which it uses to
  manage Binder environment images.

With that being said, there are three primary things that need to happen any
time someone clicks a Binder link.

1. A Docker image for the link must exist in Binder's image registry. If an image
   for the current `ref` of the repository *doesn't* exist, one will be built
   and registered automatically using `repo2docker`. If your
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
an updated `ref`. They take roughly decreasing amounts of time to complete,
so 1 >> 2 >> 3 in terms of how long each operation takes.

If Binder sessions take a while to start, but you know that your image has
already been built, there's a good chance you are in step 2, and the server is
still pulling the image onto the node that you'll be using. Please be patient!

### Will repos with fewer notebooks launch faster? Should I split my notebooks into smaller repos?

Number of notebooks in a repo shouldn't have any impact on binder launch time,
assuming a docker image for that repo is already built. It is worth noting, however,
that there is a limit to the number of instances of a repository that can be active
at any moment in time.

### Will repos that are launched often get prioritized and launch faster?

There isn't any intentional prioritization for repos that are launched frequently,
however, in practice the repos that launch more often will tend to launch faster.
This is because if a user pod is put on a node that doesn't already have the Docker
image for that repo, then it'll have to do a Docker pull first, which takes time. If
a repo is launched a lot, then most likely it will already be on a given node.


## Funding and support

### Is `mybinder.org` free to use?

Yes! Though note that it has {ref}`limited computational resources
<user_memory>`.

### How much does running `mybinder.org` cost?

If you're interested in the technical costs of running
`mybinder.org`, we publish a semi-up-to-date dataset of our costs at the
[binder-data](https://github.com/jupyterhub/binder-data/tree/master/billing/data/proc)
repository. In addition, you can explore these costs with the binder link below!

```{image} https://mybinder.org/badge_logo.svg
:target: https://mybinder.org/v2/gh/jupyterhub/binder-billing/master?urlpath=lab/tree/analyze_data.ipynb
```

### How can `mybinder.org` be free to use?
[`mybinder.org`](https://mybinder.org) relies on the generosity of donors and volunteers.
If you would like to make a donation see [](support.md).

See {ref}`about` for more information on the mybinder.org team and who provides
the resources to pay for the service. Generally, mybinder.org is run with modest resources
provided to users in order to keep costs down. In the future we hope to see more
public BinderHub services running that can form a collection of community
resources for interactive cloud computing.

## Security and privacy

[mybinder.org](https://mybinder.org) allows users to execute arbitrary code, including some outgoing network traffic.
Users can upload additional files from their computer, fetch files from remote machines and upload files to remote machines.

Providing a massively open public service like this also opens the opportunity for others to abuse our platform.
We've taken care to avoid being used as [a link in an attack chain](https://en.wikipedia.org/wiki/Kill_chain#Cyber), or otherwise being abused, and haveput several safeguards in place.
This section describes several aspects of using mybinder.org in a secure fashion.

:::{admonition} If you've found a security problem
Please see [](security:report).
:::

### An overview of Binder's security

Below is a short overview of major security efforts.

1. We limit outgoing bandwidth per-session (`~1mbit`) to protect against being used as a DDoS vector.
2. We limit launches originating from most cloud providers to prevent being used automatically in various attacks.
3. We have anti-cryptomining safeguards that automatically detect and kill processes associated with mining.
4. We ban malicious repositories from being launched when they are brought to our attention.
5. We impose general resource limits (inactivity culling timeouts, memory / CPU limits, max concurrent launches, etc) to make us a less tempting target for these attacks.
6. We do not offer persistent storage of any sort, to protect us from becoming a host for malware.

We're a volunteer run open infrastructure project, and welcome more engagement on how we can be better good citizens of the internet.
If you've discovered a security problem on [mybinder.org](https://mybinder.org), please see [](security:report).

### How we ensure user privacy

We take user privacy very seriously! Because Binder runs as a public,
free service, we don't require any kind of log-in that would let us
keep track of user data. All code that is run, data analyzed, papers
reproduced, classes taught - in short, everything that happens in a
Binder session - is destroyed when the user logs off or becomes inactive
for more than a few minutes.

Here are the pieces of information we do keep:

- We run google analytics with anonymized IPs and no cookies, which gives us just enough information to know how Binder is being used, and but won't be able to identify users.
- We retain logs of IP addresses for 30 days, which is used solely in the case of detecting abuse of the service.

If you have suggestions for how we can ensure the privacy of our data and users, we'd love to hear it!

### How secure is mybinder.org?

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
Binder instance, consider [deploying a BinderHub for your group](https://binderhub.readthedocs.io/en/latest/).

(security:report)=
### Report a security issue

If you find a security vulnerability in with `mybinder.org`, please report
it to [security@ipython.org](mailto:security@ipython.org).

If you prefer to encrypt your security reports, you can use [this PGP public key](https://jupyter-notebook.readthedocs.io/en/stable/_downloads/ipython_security.asc).

### Can I push data from my Binder session back to my repository?

While it is *technically* possible to push information from a Binder
session onto a platform like GitHub, we *strongly discourage* it. We
cannot guarantee the security of data moving through `mybinder.org`,
and your password or any sensitive data may be compromised. You
shouldn't do anything on `mybinder.org` that you wouldn't mind sharing
with the world!

## Abuse policies

### Temporary Banning

Temporary banning means that `mybinder.org` will stop building / serving Binder
sessions for a given repository. This usually happens because of some
undesired behavior with the repository. Some examples of behavior that could
result in temporary banning include:

* A large, unexpected spike in traffic that persists over time.
* Sessions that routinely use a large amount of CPU.
* Sessions that attempt to perform a lot of outgoing networking traffic.

The `mybinder.org` team uses the following workflow in discussing / deciding
when to temporarily ban a repository:

* An issue is created to document why a repo (or group of repos) is being banned
* A PR that implements the ban is opened
* A "bans" tag notes any PRs that created a ban
* The issue stays open until the ban is lifted

If you are temporarily banned, contact us on the
[Gitter Channel](https://gitter.im/jupyterhub/binder) or
[Open an Issue](https://github.com/jupyterhub/mybinder.org-deploy/issues) to discuss
how to un-ban the repository.


### Using mybinder.org as backend for your service

:::{admonition} A note on for-profit services
:class: warning

Please do not use `mybinder.org` as backend for your for-profit service or product.

The cloud resources consumed by `mybinder.org` are funded through donations or grants. Because of this we can not subsidise for-profit products or services by offering free cloud resources to them. This means we will prevent you from using `mybinder.org` as a service for your product.

Operating `mybinder.org` relies on the good will of volunteers and organisations to obtain the
resources required to do so. This is easier if we are not seen as supporting for-profit services
that are not a net contributor to the service.
:::

You may be considering using `mybinder.org` as a part of your service or product. We think that is great, and encourage people to experiment with using Binder technology as a part of their tools.

However, depending on the size and consistency of traffic being directed at `mybinder.org`, we may restrict your usage of the `mybinder.org` service in order to avoid being overloaded by a single user / organization. This is particularly true for services that trigger many **repository builds**.

In general, please be respectful of the Binder Project's limited resources. Do not forget that it has no dedicated funding and runs entirely on donations of cloud resources. If you have a question about this, please [Open an Issue](https://github.com/jupyterhub/mybinder.org-deploy/issues/new?labels=impact&template=request_resources.md).

### Report Abuse

If you'd like to report any abuse of the `mybinder.org` service, please
[click here to send an abuse report](mailto:binder-team@googlegroups.com?subject=[ABUSE]%20your-message-here).
