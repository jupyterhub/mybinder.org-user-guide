# `mybinder.org` Usage Guidelines

This page details some guidelines and policies that we follow at ``mybinder.org``.

:::{admonition,warning} When in doubt, open an issue
If you're not sure whether your use-case is reasonable for `mybinder.org`, don't
hesitate to [open an issue](https://github.com/jupyterhub/mybinder.org-deploy/issues/new?labels=question&template=ban_check.md)
to ask if your planned usage is OK.
:::

## Temporary Banning

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

## Running events with `mybinder.org`

If you'd like to run an event with `mybinder.org` and expect more than 50 users
to join at once, please [request an increase in quota for your repository](https://github.com/jupyterhub/mybinder.org-deploy/issues/new?labels=impact&template=request_resources.md).

The Binder Team occasionally increases the number of sessions that can run for a single repository if it is being used for purposes that align with the mission of the Binder Project. However, there is no guarantee that this will be done for your event.

## Maximum Concurrent Users for a Repository

We don't want a single repository to dominate all of the traffic to Binder, so
we've set a maximum limit of concurrent user sessions that point to the same
Binder link. **The maximum number of simultaneous users for a given repo is 100**.
If you think you have a *really* good reason for why this number should be
higher, please [Open an Issue](https://github.com/jupyterhub/mybinder.org-deploy/issues).
to discuss with the community!

## Maximum Concurrent Users for a Service

You may be considering using `mybinder.org` as a part of your service or product.
Think that is great, and encourage people to experiment with using Binder technology
as a part of their tools.

However, depending on the size and consistency of traffic being directed at `mybinder.org`,
we may restrict your usage of the `mybinder.org` service in order to avoid being overloaded
by a single user / organization. This is particularly true for services that trigger many **repository builds**.

In general, please be respectful of the Binder Project's limited resources. Do not forget
that it has no dedicated funding and runs entirely on donations of cloud resources.

## Reporting Abuse

If you'd like to report any abuse of the `mybinder.org` service, please
[click here to send an abuse report](mailto:binder-team@googlegroups.com?subject=[ABUSE] your-message-here).
